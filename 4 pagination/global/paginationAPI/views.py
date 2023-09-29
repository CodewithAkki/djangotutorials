from paginationAPI.models import order_models
from paginationAPI.serializers import order_serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer


class order_get_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
