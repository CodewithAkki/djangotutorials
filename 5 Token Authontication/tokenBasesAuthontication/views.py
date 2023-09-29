from rest_framework.viewsets import ModelViewSet
from .serializers import user_serializer
from .models import user_model

class user_view(ModelViewSet):
    queryset=user_model.objects.all()
    serializer_class=user_serializer