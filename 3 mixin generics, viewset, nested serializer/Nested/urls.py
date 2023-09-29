from django.urls import path
from Nested import views
urlpatterns = [
    path('books/',views.books_list_create.as_view()),
    path('books/<int:pk>/',views.books_get_update_delete.as_view()),
    path('authors/',views.authors_list_create.as_view()),
    path('author/<int:pk>/',views.authors_get_update_delete.as_view()),
    path('customer/',views.customer_list_create.as_view()),
    path('customer/<int:pk>/',views.customer_get_update_delete.as_view()),
    path('order/',views.order_list_create.as_view()),
    path('order/<int:pk>/',views.order_get_update_delete.as_view()),
]
