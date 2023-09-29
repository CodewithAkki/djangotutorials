from django.db import models
import uuid
# Create your models here.
class StudentData(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    name=models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    Designation=models.CharField(max_length=200)
    
class ImportExport(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    files=models.FileField()
