from django.urls import path
from .views import signup, ClientSignUp, EmployeeSignUp, DetailProfile, UserUpdate, Profile
from django.contrib.auth import login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/client', ClientSignUp.as_view(), name='signup-client'),
    path('signup/employee', EmployeeSignUp.as_view(), name='signup-employee'),
    path('profile/<int:user_id>', DetailProfile, name='detail'),
    path('myprofile/', Profile.as_view(), name='user-profile'),
    path('update/', UserUpdate.as_view(), name='update-user'),
]