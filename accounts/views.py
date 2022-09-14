import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from . models import User
from . serializers import UserSerializer

# Create your views here.

def handleLogin(request):
    return None
# @csrf_exempt
@api_view(['GET','POST'])
def handleRegistration(request):
    if request.method == 'GET':
        user= User.objects.all()
        # print('user',user)
        userSr = UserSerializer(user, many=True).data
        print('usersr',userSr)
        data = []
        for u in userSr:
            newUser = {
                'id': u['id'],
                'first_name': u['first_name'],
                'last_name': u['last_name'],
                'username': u['username'],
                'email': u['email']
            }
            data.append(newUser)
        return Response({'success':True, 'data':data, 'status':status.HTTP_200_OK})
    elif request.method == 'POST':
        payload = json.loads(request.body.decode('utf-8'))
        serializer = UserSerializer(data=payload)
        print('serp',serializer)
        print('pay',payload)
        
        return Response({
            'success': True,
            'status': status.HTTP_201_CREATED,
            'data':[]
        })
    return None