from django.urls import path
from django.contrib.auth import login
from .views import Schedule, Services, DeleteServices, UpdateSchedule, Budget, UpdateBudget

urlpatterns = [
    path('<int:user_id>', Services, name='services'),
    path('delete', DeleteServices.as_view, name='services-delete'),
    path('schedule/<int:employee_id>', Schedule, name='schedule'),
    path('schedule/<int:employee_id>/edit', UpdateSchedule.as_view(), name='schedule-update'),
    path('budget/<int:employee_id>', Budget, name='budget'),
    path('budget/<int:employee_id>/edit', UpdateBudget.as_view(), name='budget-update'),
]