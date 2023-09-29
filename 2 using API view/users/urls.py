from django.urls import path
from users import views
urlpatterns = [
    path("",views.users_list_create.as_view()),
    path("<pk>/",views.user_get_update_delete.as_view()),
]
'''
RuntimeError: You called this URL via PUT, but the URL doesn't end in a slash and
you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining 
PUT data. Change your form to point to localhost:8000/users/2/ (note the trailing slash),
or set APPEND_SLASH=False in your Django settings.
'''