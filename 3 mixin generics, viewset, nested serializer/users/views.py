from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,mixins
from users.models import user_model
from users.serializers import user_serilaizer
# Create your views here.
class user_list_create(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = user_model.objects.all()
    serializer_class=user_serilaizer

    def get(self,request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    

class user_get_update_delete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = user_model.objects.all()
    serializer_class= user_serilaizer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def patch(self,request,pk):
        return self.update(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
