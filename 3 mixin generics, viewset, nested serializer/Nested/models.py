from django.db import models

# Create your models here.
class authors_models(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class books_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author= models.ForeignKey(authors_models,on_delete=models.CASCADE,related_name='books')

class customers_model(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)

class orders_model(models.Model):
    id=models.AutoField(primary_key=True)
    product=models.CharField(max_length=200)
    quantity=models.IntegerField()
    customer=models.ForeignKey(customers_model,on_delete=models.CASCADE,related_name='orders')
    
