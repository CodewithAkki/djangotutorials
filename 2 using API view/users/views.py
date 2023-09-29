from django.shortcuts import render
import users.serializers as usersSerializer
import users.models as usersModels
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.

class users_list_create(APIView):
    def get(self,request,*args, **kwargs):
        try:
            student_model_object=usersModels.student.objects.all()
            serializer_object=usersSerializer.user_serializer(data=student_model_object,many=True)
            serializer_object.is_valid()
            if serializer_object:
                return Response({'users':serializer_object.data,'status':status.HTTP_200_OK})
            return Response({'users':serializer_object.data,'status':status.HTTP_400_BAD_REQUEST})
        except usersModels.student.DoesNotExist as e:
                return Response({'users':serializer_object.data,'status':status.HTTP_204_NO_CONTENT})

    def post(self,request,*args, **kwargs):
            serializer_object=usersSerializer.user_serializer(data=request.data)
            if serializer_object.is_valid():
                serializer_object.save()
                return Response({'users':serializer_object.data,'status':status.HTTP_200_OK})
            return Response({'users':serializer_object.errors,'status':status.HTTP_400_BAD_REQUEST})

class user_get_update_delete(APIView):
    def get_object(self,pk):
        try:
            return usersModels.student.objects.get(pk=pk)
        except usersModels.student.DoesNotExist:
            raise Http404
        
    def get(self,request,*args,**kwargs):
            model_object=self.get_object(kwargs['pk'])
            serializer_object=usersSerializer.user_serializer(model_object)
            if serializer_object:
                return Response({'users':serializer_object.data,'status':status.HTTP_200_OK})
            return Response({'users':serializer_object.data,'status':status.HTTP_400_BAD_REQUEST})

    def patch(self,request,*args,**kwargs):
            models_object=self.get_object(kwargs['pk'])
            serializer_object=usersSerializer.user_serializer(models_object,data=request.data,partial=True)
            if serializer_object.is_valid():
                serializer_object.save()
                return Response({'users':serializer_object.data,'status':status.HTTP_200_OK})
            return Response({'users':serializer_object.errors,'status':status.HTTP_400_BAD_REQUEST})

    def put(self,request,*args,**kwargs):
            models_object=self.get_object(kwargs['pk'])
            serializer_object=usersSerializer.user_serializer(models_object,data=request.data)
            if serializer_object.is_valid():
                serializer_object.save()
                return Response({'users':serializer_object.data,'status':status.HTTP_200_OK})
            return Response({'users':serializer_object.errors,'status':status.HTTP_400_BAD_REQUEST})

    def delete(self,request,*args,**kwargs):
            models_object=self.get_object(kwargs['pk'])
            models_object.delete()
            serializer_object=usersSerializer.user_serializer(models_object)
            return Response({'users':serializer_object.data,'status':status.HTTP_204_NO_CONTENT})
         
           
                 
      
            




