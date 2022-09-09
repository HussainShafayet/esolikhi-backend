
from .models import Posts
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title','details']
    
        