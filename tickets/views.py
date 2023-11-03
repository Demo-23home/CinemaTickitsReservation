from django.http import JsonResponse
from django.shortcuts import render
#Internal Imports
from .models import Guest, Movie, Reservation
from .serializers import GuestSerializer, MovieSerailizer, ReservationSerializer
#RestFramework imports
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response


#1 without REST and no ModleQuery
def no_rest_no_model(request):

    guests = [
        {
            'id': 1,
            "name" : "Zeyad",
            "mobile" : "01017595972"
        },

        {
            'id': 2,
            "name" : "Mohammed",
            "mobile" : "01017595973"
        }
    ]


    return JsonResponse(guests, safe=False)




#2 no REST from models
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests' : list(data.values('name', 'phone'))
    }
    return JsonResponse(response)




#3 Function Based Views

#3.1 GET, POST
@api_view(['GET','POST'])
def fbv_list(request):
    
    #GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method == "POST":
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




#3.2 GET, PUT, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def fbv_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == "GET":
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    if request.method == "PUT":
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erorrs, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    if request.method == "DELETE":
        guest.delete()
        return Response(status=status.HTTP_200_OK)
    