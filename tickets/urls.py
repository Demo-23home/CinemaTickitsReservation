from django.urls import path
from .views import *



urlpatterns = [
    
    #1
    path('django/jsonresponsenomodel/', no_rest_no_model),
    #2
    path('django/jsonresponsefrommodel/',no_rest_from_model),
    #3
    path('rest/fbv_list/',fbv_list),
    #4
    path('rest/fbv_pk/<int:pk>', fbv_pk),

]





