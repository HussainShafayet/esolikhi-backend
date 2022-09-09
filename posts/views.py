import json
from django.views.decorators.csrf import csrf_exempt
from .models import Posts
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Postserializer



# Create your views here.

@csrf_exempt
@api_view(['POST','GET'])
def posts(request):
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = Postserializer(posts, many=True).data
        data= []
        for post in serializer:
            obj ={
                'id':post['id'],
                'title':post['title'],
                'details':post['details']
            }
            data.append(obj)
        return Response({'status':status.HTTP_200_OK,"succes":True,"data":data})
    elif request.method == 'POST':
        payload = json.loads(request.body.decode('utf-8'))
        # title = payload['title']
        # details = payload['details']
        # new_post = Posts()
        # new_post.title = title
        # new_post.details = details
        # new_post.save()
        serializer = Postserializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":status.HTTP_201_CREATED,
                "message":"Post added successfully",
                'data':payload,
                })
    
