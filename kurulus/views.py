from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Kurulus
from .serializers import ItemSerializer

from .models import Kurulus
from .forms import kurulusForm

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

# Retrieve kurulus list
def kurulus_filter(request):
    KurulusTuru_ = request.GET.get('KurulusTuru')
    kurulus = Kurulus.objects.filter(KurulusTuru= KurulusTuru_)
    return {"kurulus": list(kurulus.values_list())}




# Retrieve kurulus list
def kurulus_list(request):
    kurulus = Kurulus.objects.all()
    return {"kurulus": list(kurulus.values_list())}







@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Get all kuruluslar': '/',
        'Search by KurulusCalisanSayi': '/?KurulusCalisanSayi=KurulusCalisanSayi',
        'Search by KurulusTuru': '/?KurulusTuru=KurulusTuru',
        'Add new kuruls': '/create',
        'Update kurulus': '/update/pk',
        'Delete kurulus': '/kurulus/pk/delete'
    }
    return Response(api_urls)

from rest_framework import serializers
from rest_framework import status

@api_view(['POST'])
def add_kurulus(request):
	kurulus = ItemSerializer(data=request.data)

	# validating for already existing data
	if Kurulus.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if kurulus.is_valid():
		kurulus.save()
		return Response(kurulus.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_kurulus(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        kurulus = Kurulus.objects.filter(**request.query_param.dict())
    else:
        kurulus = Kurulus.objects.all()
  
    # if there is something in items else raise error
    if kurulus:
        data = ItemSerializer(kurulus)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
  


@api_view(['POST'])
def update_kurulus(request, pk):
    kurulus = Kurulus.objects.get(pk=pk)
    data = ItemSerializer(instance=kurulus, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['DELETE'])
def delete_kurulus(request, pk):
    kurulus = get_object_or_404(Kurulus, pk=pk)
    kurulus.delete()
    return Response(status=status.HTTP_202_ACCEPTED)