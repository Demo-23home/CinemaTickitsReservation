#Django imports
from django.http import JsonResponse, Http404
from django.shortcuts import render
#Internal Imports
from .models import Guest, Movie, Reservation, Post
from .serializers import GuestSerializer, MovieSerailizer, ReservationSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly
#RestFramework imports
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


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
    



#4 Class Based Views

#4.1 List and Create
class CBVList(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


#4.2 get, put and delete
class CBVPk(APIView):
    def get_object(self, pk):
        try:
            guest = Guest.objects.get(pk=pk)
            return guest
        except Guest.DoesNotExist:
            raise Http404
        
    
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
        
        


#5 Mixins

#5.1 mixins list and create
class Mixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)


#5.2 mixins retreive update create
class MixinsPk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer



    def get(self, request, pk):
        return self.retrieve(request)
    
    def put(self, request, pk):
        return self.update(request)
    
    def delete(self, request, pk):
        return self.destroy(request)





#6 Generics

#6.1 get and post
class GenericListCreate(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


#6.2 get, put, delete
class GenericPk(generics.RetrieveUpdateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


#7 Viewsets
class GeuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerailizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']
 

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer 




#8 find Movie
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        movie = request.data['movie'],
    )
    serializer = MovieSerailizer(movies, many=True)
    return Response(serializer.data)


#9 create new reservation
@api_view(['POST'])
def create_reservation(request):

    movie = Movie.objects.get(
        Hall = request.data['Hall'],
        movie = request.data['movie'],
    )

    guest = Guest()
    # guest.id = request.data['id']
    guest.name = request.data['name']
    guest.phone = request.data['phone']
    guest.save()

    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()
    
    return Response(status=status.HTTP_201_CREATED)





class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer