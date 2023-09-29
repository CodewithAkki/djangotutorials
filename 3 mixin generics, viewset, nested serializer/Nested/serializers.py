from rest_framework import serializers
from Nested.models import books_model, authors_models, orders_model, customers_model
class book_serializer(serializers.ModelSerializer):
    class Meta:
        model=books_model
        fields= '__all__'

class author_serializer(serializers.ModelSerializer):
    books=book_serializer(read_only=True,many=True)
    class Meta:
        model=authors_models
        fields='__all__'

class order_serializer(serializers.ModelSerializer):
    class Meta:
        model=orders_model
        fields='__all__'

class customer_serializer(serializers.ModelSerializer):
    orders=order_serializer(read_only=True,many=True)
    class Meta:
        model=customers_model
        fields='__all__'