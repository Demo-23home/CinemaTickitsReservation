from django.db import router
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('guests', GeuestViewSet)
router.register('movies', MovieViewSet)
router.register('reservations', ReservationViewSet)




urlpatterns = [
    
    #1
    path('django/jsonresponsenomodel/', no_rest_no_model),
    #2
    path('django/jsonresponsefrommodel/',no_rest_from_model),
    #3.1
    path('rest/fbv_list/',fbv_list),
    #3.2
    path('rest/fbv_pk/<int:pk>', fbv_pk),
    #4.1
    path('rest/cbv',CBVList.as_view()),
    #4.2
    path('rest/cbv_pk/<int:pk>/',CBVPk.as_view()),
    #5.1
    path('rest/mixins/',Mixins.as_view()),
    #5.2
    path('rest/mixins_pk/<int:pk>/',MixinsPk.as_view()),
    #6.1
    path('rest/generics/',GenericListCreate.as_view()),
    #6.2
    path('rest/generic_pk/<int:pk>/',GenericPk.as_view()),
    #7 Viewsets
    path('rest/viewsets/',include(router.urls)),
    #8 find movie
    path('fbv/find_movie',find_movie),
    #9 new reservation
    path('new_reservation/',create_reservation),
]





