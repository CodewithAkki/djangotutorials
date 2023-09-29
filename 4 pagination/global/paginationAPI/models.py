from django.db import models


class order_models(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
