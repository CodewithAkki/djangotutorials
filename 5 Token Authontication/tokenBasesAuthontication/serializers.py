from rest_framework import serializers
from .models import user_model

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=user_model
        fields='__all__'

