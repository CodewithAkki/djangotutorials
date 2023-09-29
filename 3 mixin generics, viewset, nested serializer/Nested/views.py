from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from Nested.models import books_model , authors_models ,customers_model,orders_model
from Nested.serializers import book_serializer ,author_serializer,order_serializer,customer_serializer
# Create your views here.

class books_list_create(ListCreateAPIView):
    queryset=books_model.objects.all()
    serializer_class=book_serializer

class books_get_update_delete(RetrieveUpdateDestroyAPIView):
    queryset=books_model.objects.all()
    serializer_class=book_serializer
  
class authors_list_create(ListCreateAPIView):
    queryset=authors_models.objects.all()
    serializer_class=author_serializer

class authors_get_update_delete(RetrieveUpdateDestroyAPIView):
    queryset=authors_models.objects.all()
    serializer_class=author_serializer

class customer_list_create(ListCreateAPIView):
    queryset=customers_model.objects.all()
    serializer_class=customer_serializer

class order_get_update_delete(RetrieveUpdateDestroyAPIView):
    queryset=orders_model.objects.all()
    serializer_class=order_serializer

class order_list_create(ListCreateAPIView):
    queryset=orders_model.objects.all()
    serializer_class=order_serializer

class customer_get_update_delete(RetrieveUpdateDestroyAPIView):
    queryset=customers_model.objects.all()
    serializer_class=customer_serializer