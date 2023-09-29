from rest_framework import serializers
from ORMPractice.models import Student
class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    def validate_username(self, attrs):
        print("validation"+attrs)
        