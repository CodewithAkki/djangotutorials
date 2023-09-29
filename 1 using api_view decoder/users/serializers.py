from rest_framework import serializers
import users.models as users_models
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model= users_models.students
        fields='__all__'
