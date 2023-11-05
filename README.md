Cinema Tickets Reservation System
<div align="center">
  <img src="link_to_your_project_logo_or_screenshot" alt="Project Logo or Screenshot">
</div>
This repository contains a simple cinema ticket reservation system that serves as a reference for REST Framework, authentication classes, and permission classes. It provides endpoints for various functionalities related to cinema ticket reservation.

Endpoints
1. No Model Endpoints
1.1 GET /django/jsonresponsenomodel/
This endpoint returns a JSON response without using any Django models.

1.2 GET /django/jsonresponsefrommodel/
This endpoint returns a JSON response using Django models.

2. Function-Based Views (FBV) Endpoints
2.1 GET /rest/fbv_list/
This endpoint uses function-based views to list items.

2.2 GET /rest/fbv_pk/<int:pk>
This endpoint uses function-based views to retrieve a specific item by its primary key.

3. Class-Based Views (CBV) Endpoints
3.1 GET, POST /rest/cbv
This endpoint uses class-based views to handle list and create operations.

3.2 GET, PUT, DELETE /rest/cbv_pk/<int:pk>/
This endpoint uses class-based views to handle retrieve, update, and delete operations for a specific item.

4. Mixins Endpoints
4.1 GET, POST /rest/mixins/
This endpoint uses mixins to handle list and create operations.

4.2 GET, PUT, DELETE /rest/mixins_pk/<int:pk>/
This endpoint uses mixins to handle retrieve, update, and delete operations for a specific item.

5. Generics Endpoints
5.1 GET, POST /rest/generics/
This endpoint uses generic views to handle list and create operations.

5.2 GET, PUT, DELETE /rest/generic_pk/<int:pk>/
This endpoint uses generic views to handle retrieve, update, and delete operations for a specific item.

6. Viewsets Endpoints
6.1 GET, POST /rest/viewsets/
This endpoint uses viewsets and routers to handle list and create operations.

7. Find Movie Endpoint
7.1 GET /fbv/find_movie
This endpoint allows you to find a specific movie.

8. New Reservation Endpoint
8.1 POST /new_reservation/
This endpoint enables you to create a new reservation.

9. REST Auth URLs
9.1 POST /api-auth/
This endpoint provides URLs for REST framework authentication views.

10. Token Authentication
10.1 POST /api-token-auth/
This endpoint allows users to obtain an authentication token.

11. Post Permissions Endpoints
11.1 GET, PUT, DELETE /post/<int:pk>
This endpoint allows operations on a specific post based on user permissions.

11.2 GET, POST /post/
This endpoint allows listing and creating posts based on user permissions.

Usage
To utilize these endpoints, make HTTP requests to the respective URLs using appropriate methods (GET, POST, PUT, DELETE) based on the desired operation.

Feel free to explore the code to understand the implementation details of the REST Framework, authentication classes, and permission classes used in this project. If you have any questions or need further assistance, don't hesitate to reach out. Happy coding!

