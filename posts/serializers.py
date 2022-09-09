
from .models import Posts
from rest_framework import serializers

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title','details']
    
        