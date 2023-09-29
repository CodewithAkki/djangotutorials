from django.shortcuts import render
from users.models import user_model
from users.serializers import user_serilaizer
from rest_framework import generics
# Create your views here.

class user_get_create(generics.ListCreateAPIView):
    queryset = user_model.objects.all()
    serializer_class= user_serilaizer

class user_get_update_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset=user_model.objects.all()
    serializer_class=user_serilaizer
