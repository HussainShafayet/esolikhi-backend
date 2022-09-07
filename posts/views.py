from cmath import log
from email import header
from email.policy import HTTP
import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def posts(request):
    
    if request.method == 'POST':
        payload = json.loads(request.body.decode('utf-8'))
        header("Access-Control-Allow-Origin: *")
    return HttpResponse('Hello this is first api')
