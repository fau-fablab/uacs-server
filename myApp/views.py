from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import fablabUser
import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def index(request):
	return HttpResponse("Hello. Pleaase attach a fauid to the URL.")

def detail(request, wantedfauid):
#requesteduser = fablabUser.objects.get(fauid=wantedfauid)
	requesteduser = get_object_or_404(fablabUser, fauid=wantedfauid)
	dictuser = requesteduser.__dict__
	dictstr = str(dictuser)
	dictserialized = serializers.serialize('json', [requesteduser, ] )
#	mydump = json.dumps([dictuser, ])
#	requesteduser = fablabUser.objects.filter(fauid=
#	userinjson = serializers.serialize("json",requesteduser)
	
#returnelement = json.loads(requesteduser)
#return HttpResponse(dictstr, content_type='text/plain')


#return HttpResponse(json.dumps(dictserialized), content_type="application/json"
	return HttpResponse(dictserialized, content_type="application/json")
#	return JsonResponse(dictserialized, safe=False)
# Create your views here.
