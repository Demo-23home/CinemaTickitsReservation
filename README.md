Cinema Tickets Reservation System
Welcome to the Cinema Tickets Reservation System repository! This project serves as a comprehensive reference guide for REST Framework, Authentication Classes, and Permission Classes in Django, specifically tailored to your needs. Here's a detailed guide to help you understand the structure and functionality of this system.

1.Table of Contents
2.Introduction
3.Features
4.Technologies Used
5.Setup Instructions
6.Project Structure
7.API Endpoints
8.Authentication and Permissions
9.Usage Examples
10.Contributing
11.License

Introduction
The Cinema Tickets Reservation System is a simple yet robust web application that allows users to reserve cinema tickets online. It demonstrates the implementation of RESTful APIs, various authentication mechanisms, and permission classes in Django. This project is designed to be your go-to reference for understanding these concepts in-depth.

Features
User authentication and authorization
Movie listing and details
Cinema hall selection
Seat reservation functionality
Booking history tracking

Technologies Used
Django: The high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django REST Framework: A powerful toolkit for building Web APIs in Django applications.
SQLite: A lightweight, disk-based database that doesn’t require a separate server process.

Setup Instructions
Clone the repository: git clone <repository_url>
Navigate to the project directory: cd cinema-tickets-reservation-system
Install dependencies: pip install -r requirements.txt
Apply database migrations: python manage.py migrate
Create a superuser for admin access: python manage.py createsuperuser
Run the development server: python manage.py runserver

Project Structure
cinema_tickets: Django application directory containing models, views, serializers, and API endpoints.
config: Django project configuration directory.
templates: HTML templates for rendering the frontend views.
static: Static files like CSS, JavaScript, and images.

API Endpoints
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
    #10 rest auth url
    path('api-auth/',include('rest_framework.urls')), 
    #11 Token Authentiaction
    path('api-token-auth/', obtain_auth_token),
    #12 post permissions
    path('post/<int:pk>',Post_pk.as_view()),
    path('post/',Post_pk.as_view()),

Authentication and Permissions
This system employs token-based authentication using Django REST Framework's Token Authentication. Only authenticated users can make seat reservations. Additionally, custom permission classes are implemented to ensure that users can only view and modify their own bookings.
