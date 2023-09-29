from django.db import models

# Create your models here.
class students(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return str(self.id)+' '+self.username+' '+str(self.salary)