from django.urls import path
from genericAPI import views
urlpatterns = [
    path("generics/",views.user_get_create.as_view()),
    path("generics/<int:pk>",views.user_get_update_delete.as_view()),
]
