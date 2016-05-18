from django.http import HttpResponse
from django.http import HttpResponseRedirect
from myApp.models import fablabUser
from myApp.models import fablabDevice
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
# from django.shortcuts import render
# from django.forms.models import model_to_dict
# import json
# from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello. Please attach a fauid to the URL.")


def devices(request, wanteddevice):
    # requesteduser = fablabUser.objects.get(cardid=wantedcardid)
    requesteddevice = get_object_or_404(fablabDevice, Name=wanteddevice)
    dictdevice = requesteddevice.__dict__
    dictstr = str(dictdevice)  # unused
    dictserialized = serializers.serialize('json', [requesteddevice, ])
    return HttpResponse(dictserialized, content_type="application/json")


def detail(request, wantedcardid):
    # requesteduser = fablabUser.objects.get(cardid=wantedcardid)
    requesteduser = get_object_or_404(fablabUser, cardid=wantedcardid)
    dictuser = requesteduser.__dict__
    dictstr = str(dictuser)  # unused
    dictserialized = serializers.serialize('json', [requesteduser, ])
#    mydump = json.dumps([dictuser, ])
#    requesteduser = fablabUser.objects.filter(fauid=
#    userinjson = serializers.serialize("json",requesteduser)


#    returnelement = json.loads(requesteduser)
#    return HttpResponse(dictstr, content_type='text/plain')
#    return HttpResponse(json.dumps(dictserialized),
#                        content_type="application/json"
    return HttpResponse(dictserialized, content_type="application/json")
#    return JsonResponse(dictserialized, safe=False)
# Create your views here.

@csrf_exempt
def create(request):
    try:
        requesteddevice = request.POST['device']  # unused
    except(KeyError):
        return HttpResponse("device does not exist")
    requestingid = request.POST['requestingid']
    requestedid = request.POST['requestedid']
    myrequestinguser = get_object_or_404(fablabUser, cardid=requestingid)
    myrequesteduser = get_object_or_404(fablabUser, cardid=requestedid)
    print("myrequestinguser")
    
    # comp = myrequestinguser.Betreuer
    if not myrequestinguser.Betreuer:
        return HttpResponse("Kein Betreuer")
    if not getattr(myrequestinguser, requesteddevice):
        return HttpResponse("Betreuer hat keine Einweisung")
    
    
    # get real database entry
    requesteduser = fablabUser.objects.get(cardid=requestedid)
    setattr(requesteduser, requesteddevice, True)
    requesteduser.save()

#return HttpResponseRedirect(reverse('done'))  # both methods are undefined
    return HttpResponse("done")  # both methods are undefined

@csrf_exempt
def newUser(request):
    try:
        newcardid = request.POST['cardid']  # unused
        requestingcardid = fablabUser.objects.get(cardid=newcardid)
        return HttpResponse("error") # get did not throw Exceptions, user already in database
    except(KeyError):
        return HttpResponse("card id was not given")
    except(ObjectDoesNotExist):
        # Card id is not present in the current database, everything alright
        # Create new user
        newuser = fablabUser(cardid=newcardid)
        newuser.save()
        return HttpResponse("done")  # both methods are undefined


@csrf_exempt
def strikeUser(request):
    try:
        userid = request.POST['user'] # User to strike
        device = request.POST['device'] # Device to strike
        
        # Load user
        user = fablabUser.objects.get(cardid=userid)

        # Load strike list
        strike_text = getattr(user, device+"_strikes") 
        strikes = strike_text.split(str=",")
        new_strike_text = datetime.now().strftime("%Y-%m-%d.%H:%M:%S")+','
        strike_count = 1

        # Cycle strike list to delete old strikes and count strikes
        for datetext in strikes:
            date = datetime.strptime(datetext, "%Y-%m-%d.%H:%M:%S")
            dyear, month = divmod(date.month+3,12)

            if month == 0:
                month=12
                dyear -= 1
            date_expiration = datetime(date.year + dyear, month, date.day,date.hour,date.minute,date.second)

            if date_expiration < datetime.now():
                # Strike is 3 months old -> delete
                pass
            else:
                # Strike is still valid
                new_strike_text += datetext+','
                strike_count += 1
            
        if new_strike_text[-1] == ',':
            # Delete invalid seperator ','
            new_strike_text = new_strike_text[:-1]

        if strike_count > 3:
            # Do something - E-mail to active fablab member - deactivate card?
            pass
        
        # Save new strike list
        setattr(user, device+"_strikes", new_strike_text)
        user.save()

        return HttpResponse("done - strike_{}".format(strike_count))
 
    except(KeyError):
        return HttpResponse("invalid request - parameter mismatch")
    except(ObjectDoesNotExist):
        # User could not be found in the database, must not happen!
        return HttpResponse("invalid request - no matching user found")
    except(AttributeError):
        # Device was not found
        return HttpResponse("invalid request - no matching device found")
    except(ValueError):
        # Error probably in datetime.strptime conversion. corrupted database?
        return HttpResponse("internal error - ValueError")

