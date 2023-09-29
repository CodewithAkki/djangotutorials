from django.urls import path,include
from users import views
urlpatterns =[
    path("",views.users_list_create),
    path("<pk>/",views.users_get_update_delete),

]

