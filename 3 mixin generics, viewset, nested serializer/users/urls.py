from django.urls import path
from users import views
urlpatterns = [
    path('users/',views.user_list_create.as_view()),
    path('users/<int:pk>/',views.user_get_update_delete.as_view()),

]
