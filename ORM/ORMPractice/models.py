from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=200,unique=True,help_text="This field must be string type")
    age = models.IntegerField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username