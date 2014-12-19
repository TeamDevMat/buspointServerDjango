import requests
import json
import os

from  buspoint import encode_json
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


# Create your views here.
def index(request):
	
	mbuspoint =encode_json()
		
	return HttpResponse('<pre>' + str(json.dumps(mbuspoint,indent = 4)) + '</pre>') 

def buspoint():
	camion_dict =  {'id':1,'latitud':23.2323,'loguitud':-43.32423,'hora':23423423}
	

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

