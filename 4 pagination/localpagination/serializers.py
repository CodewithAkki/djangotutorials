from rest_framework import serializers
from localpagination.models import order_models

class order_serializer(serializers.ModelSerializer):
    class Meta:
        model = order_models
        fields = "__all__"
