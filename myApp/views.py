from django.http import HttpResponse
from django.http import HttpResponseRedirect
from myApp.models import fablabUser
from myApp.models import fablabDevice
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
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
def create(request, user):
    try:
        requesteddevice = request.POST['device']  # unused
    except(KeyError):
        return HttpResponse("device does not exist")
    requestingid = request.POST['requestingid']
    requestedid = request.POST['requestedid']
    myrequestinguser = get_object_or_404(fablabUser, fauid=requestingid)
    myrequesteduser = get_object_or_404(fablabUser, fauid=requestedid)
    print("myrequestinguser")
    # comp = myrequestinguser.Betreuer
    if not myrequestinguser.Betreuer:
        return HttpResponse("Kein Betreuer")
    if not myrequestinguser.requesteddevice:
        return HttpResponse("Betreuer hat keine Einweisung")
    myrequesteduser.device = True
    myrequesteduser.save()
    return HttpResponseRedirect(reverse('done'))  # both methods are undefined
