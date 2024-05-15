from django.urls import path
from .views import user_login , user_logout , user_signup

urlpatterns = [
    path('' , user_login , name='login'  )  ,
    path('logout/', user_logout, name='logout'),
    path('signup/', user_signup, name='signup'),
]
