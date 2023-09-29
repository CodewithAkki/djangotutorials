from django.db import models
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

class user_model(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=200,unique=True)
    salary=models.DecimalField(max_digits=13,decimal_places=3)

    def __str__(self):
        return self.username

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)    
