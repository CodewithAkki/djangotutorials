from django.http import JsonResponse
import users.models as users_models
from rest_framework import status
from rest_framework.decorators import api_view
import users.serializers as users_serializer
# Create your views here.
@api_view(['GET','POST'])
def users_list_create(request):
    match request.method :
        case 'GET': 
            users_object = users_models.students.objects.all()
            users_serializer_object=users_serializer.user_serializer(users_object,many=True)
            if users_serializer_object:
                response={'students':users_serializer_object.data,"status":status.HTTP_201_CREATED}
                return JsonResponse(response)
            return JsonResponse({"students":[],"status":status.HTTP_204_NO_CONTENT})
            
        case 'POST':
            try:
                users_serializer_object=users_serializer.user_serializer(data=request.data)
                print(users_serializer_object)
                if users_serializer_object.is_valid():
                    users_serializer_object.save()
                    return JsonResponse({"students":users_serializer_object.data,"status":status.HTTP_201_CREATED})
                else:
                    return JsonResponse({"error":users_serializer_object.errors,"status":status.HTTP_400_BAD_REQUEST})
            except Exception as e:
                print(e)
                return JsonResponse({"status":status.HTTP_400_BAD_REQUEST})

@api_view(['GET','PUT','PATCH','DELETE'])
def users_get_update_delete(request,pk):
            try:
                users_objects = users_models.students.objects.get(pk=pk)
            except users_models.students.DoesNotExist:
                return JsonResponse({"students":[],"status":status.HTTP_404_NOT_FOUND})
            
            match request.method:
                case 'GET':
                    users_serializer_object= users_serializer.user_serializer(users_objects)
                    if users_serializer_object:
                        return JsonResponse({"student":users_serializer_object.data,"status":status.HTTP_202_ACCEPTED})
                    else:
                        return JsonResponse({"error":users_serializer_object.errors,"status":status.HTTP_202_ACCEPTED})    
                case 'PUT':
                    users_serializer_object= users_serializer.user_serializer(users_objects,data=request.data)
                    if users_serializer_object.is_valid():
                        users_serializer_object.save()
                        return JsonResponse({"student":users_serializer_object.data,"status":status.HTTP_202_ACCEPTED})
                    return JsonResponse({"error":users_serializer_object.errors,"status":status.HTTP_400_BAD_REQUEST})
                case 'PATCH':
                        users_serializer_object= users_serializer.user_serializer(users_objects,data=request.data,partial=True)
                        if users_serializer_object.is_valid():
                            users_serializer_object.save()
                            return JsonResponse({"student":users_serializer_object.data,"status":status.HTTP_202_ACCEPTED})
                        return JsonResponse({"error":users_serializer_object.errors,"status":status.HTTP_400_BAD_REQUEST})
                case 'DELETE':
                    users_serializer_object= users_serializer.user_serializer(users_objects)
                    users_objects.delete()
                    return JsonResponse({"student":users_serializer_object.data,"status":status.HTTP_202_ACCEPTED})
                    


    

