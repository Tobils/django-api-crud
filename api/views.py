from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status

from .models import Item
from .serializers import ItemSerializer

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
  api_urls = {
    'all_items': '/',
    'Search By Category': '/?category=vategory_name',
    'Search By Subcategory': '/?subcategory=category_name',
    'Add': '/create',
    'Update': '/update/pk',
    'Delete': '/item/pk/delete'
  }
  return Response(api_urls)


@api_view(['POST'])
def add_items(request):
  item = ItemSerializer(data=request.data)
  if item.objects.filter(**request.data).exists():
    raise serializers.ValidationError('This data already exists')
  if item.is_valid():
    item.save()
    return Response(item.data)
  else:
    return Response(status=status.HTTP_404_NOT_FOUND)


class ContactForm(serializers.Serializer):
      # simple serializer for emails
    email = serializers.EmailField()
    message = serializers.CharField()
  
  
@api_view(['POST','GET'])
@swagger_auto_schema(request_body=ContactForm)
def sendEmail(self, request):
      # serializer object
    serializer = ContactForm(data=request.data)
    # checking for errors
    if serializer.is_valid():
        json = serializer.data
        return Response(
            data={"status": "OK", "message": json},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)