from localpagination.models import order_models
from localpagination.serializers import order_serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

class pagination(PageNumberPagination):
    page_size=2

class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
    pagination_class=LimitOffsetPagination
    filter_backends=[filters.OrderingFilter,filters.SearchFilter]
    search_fields=['^name']
    ordering_fields=['name','quantity']#-field name for deciending order
    ordering=['-id']# default ordering
    


'''
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 2,
    "DEFAULT_AUTHONTICATION_CLASSES":["rest_framework.authontication.BasicAuthontication"],
    "DEFAUTL_PERMISSION_CLASSES":["rest_framework.permissions.IsAuthonticated"],
}

You can configer it global level

class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
    pagination_class=LimitOffsetPagination
    filter_backends=[filters.OrderingFilter,filters.SearchFilter]
    search_fields=['^name']
    ordering_fields=['name','quantity']#-field name for deciending order
    ordering=['-id']# default ordering
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

'''


'''
class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
    pagination_class=LimitOffsetPagination
    filter_backends=[filters.OrderingFilter,filters.SearchFilter]
    search_fields=['^name']
    ordering_fields=['name','quantity']#-field name for deciending order
    ordering=['-id']# default ordering
'''

'''
class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
    pagination_class=LimitOffsetPagination
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['name','quantity']#-field name for deciending order
    ordering=['-id']# default ordering

'''
'''

class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
    pagination_class=LimitOffsetPagination
    filter_backends=[filters.SearchFilter]
    search_fields=['^name','=quantity']

more about search_fields 
^ : start with
= : Exact match
@ : full-text search (only support for postgresql backend)
$ : regular expression search 

'''

'''
class order_list_create(ListCreateAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
    pagination_class=LimitOffsetPagination
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['name','quantity']
'''

class order_get_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = order_models.objects.all()
    serializer_class = order_serializer
