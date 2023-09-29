from django.db import models

# Create your models here.
class student (models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    salary= models.DecimalField(max_digits=10,decimal_places=3)
    def __str__(self):
        return str(self.id)+' '+self.username+' '+str(self.salary)
     