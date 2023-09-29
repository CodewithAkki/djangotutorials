from rest_framework import serializers
from users.models import user_model
class user_serilaizer(serializers.ModelSerializer):
    class Meta:
        model=user_model
        fields='__all__'