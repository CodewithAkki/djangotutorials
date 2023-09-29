from rest_framework import serializers
from traditional.models import StudentData,ImportExport
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentData
        fields='__all__'

class ImportExportSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImportExport
        fields='__all__'