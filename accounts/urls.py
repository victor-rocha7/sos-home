from django.urls import path
from .views import signup, ClientSignUp, EmployeeSignUp
from django.contrib.auth import login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/client', ClientSignUp.as_view(), name='signup-client'),
    path('signup/employee', EmployeeSignUp.as_view(), name='signup-employee'),
]