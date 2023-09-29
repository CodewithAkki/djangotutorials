from django.shortcuts import render
from rest_framework import viewsets
from users.models import user_model
from users.serializers import user_serilaizer
# Create your views here.

class user_viewset(viewsets.ModelViewSet):
    queryset = user_model.objects.all()
    serializer_class=user_serilaizer

class user_reade_set(viewsets.ReadOnlyModelViewSet):
    queryset=user_model.objects.all()
    serializer_class=user_serilaizer

