from rest_framework import serializers
import users.models as usermodels
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=usermodels.student
        fields='__all__'