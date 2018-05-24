from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework import status
from .serializers import PuppySerializer
from .models import Puppy
# Create your views here.


@api_view(['GET','DELETE','PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #getting details of a single item
    if request.method == 'GET':
        return Response({}) 
    #deleting details of a single item
    elif request.method == 'DELETE':
        return Response({})
    #updating details of a single item
    elif request.method == 'PUT':
        return Response({})
    

@api_view(['GET','POST'])
def get_post_puppies(request):
    #get all items
    if request.method == 'GET':
        return Response({})
    
    #inserting a new record 
    elif request.method == 'POST':
        return Response({})
