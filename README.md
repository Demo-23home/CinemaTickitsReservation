# Cinema Tickets Reservation System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This is a Django REST Framework-based cinema tickets reservation system project.

## Project Overview

This project serves as a reference for REST Framework, authentication classes, and permission classes. It provides various endpoints for cinema ticket reservation, including functionalities like listing movies, creating reservations, and managing permissions.

## Features

- **No Model Endpoints:** JSON responses without using Django models.
- **Function-Based Views (FBV) Endpoints:** Using function-based views for listing and retrieving items.
- **Class-Based Views (CBV) Endpoints:** Using class-based views for handling list, create, retrieve, update, and delete operations.
- **Mixins Endpoints:** Utilizing mixins for handling CRUD operations.
- **Generics Endpoints:** Using generic views for handling CRUD operations.
- **Viewsets Endpoints:** Using viewsets and routers for handling CRUD operations.
- **Find Movie Endpoint:** Endpoint for finding a specific movie.
- **New Reservation Endpoint:** Endpoint for creating a new reservation.
- **REST Auth URLs:** Authentication views provided by REST framework.
- **Token Authentication:** Endpoint for obtaining authentication tokens.
- **Post Permissions Endpoints:** Endpoints for operations based on user permissions.

## Getting Started

To set up and run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Demo-23home/CinemaTickitsReservation.git
   cd CinemaTickitsReservation

1.Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
2.Apply migrations and create a superuser:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
3.Start the development server:
```
python manage.py runserver
```
**API Endpoints**
1.List Movies:

*URL: /api/movies/
*HTTP Method: GET
*Description: List all available movies.

2.Create Reservation:

*URL: /api/reservations/
*HTTP Method: POST
*Description: Create a new reservation.

3.Find Movie:

*URL: /api/find_movie/
*HTTP Method: GET
*Description: Find a specific movie by its title.

4.Authentication:

*URL: /api-token-auth/
*HTTP Method: POST
*Description: Obtain an authentication token.

