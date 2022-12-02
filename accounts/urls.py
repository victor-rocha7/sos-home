from django.urls import path
from .views import signup, ClientSignUp, EmployeeSignUp, DetailProfile, UserUpdate, Profile, Rate, UpdateRate, DeleteRate
from django.contrib.auth import login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/client', ClientSignUp.as_view(), name='signup-client'),
    path('signup/employee', EmployeeSignUp.as_view(), name='signup-employee'),
    path('profile/<int:user_id>', DetailProfile, name='detail'),
    path('myprofile/', Profile, name='user-profile'),
    path('update/', UserUpdate.as_view(), name='update-user'),
    path('profile/<int:user_id>/rate', Rate, name='rate-profile'),
    path('profile/<int:user_id>/rate/edit/<int:pk>', UpdateRate.as_view(), name='rate-update'),
    path('profile/<int:user_id>/rate/delete/<int:pk>', DeleteRate.as_view(), name='rate-delete'),
]