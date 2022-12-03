from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from accounts.models import User, Employee, Client
from .models import Services
from .forms import ScheduleForm, UpdateScheduleForm, BudgetForm, UpdateBudgetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Services(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_client:
        client = user
    elif user.is_employee:
        employee = user
    return render(request, 'services.html')

class DeleteServices(DeleteView):
    model = Services
    template_name = 'delete_services.html'

    def get_success_url(self):
        return reverse('services', kwargs={'user_id': self.object.profile_id})

@login_required
def Schedule(request, employee_id):
    employee = Employee.objects.get(user_id=employee_id)
    client = Client.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form=ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.job_date_time = form.cleaned_data['job_date_time']
            schedule.client = client
            schedule.employee = employee
            schedule.save()
            return HttpResponseRedirect(reverse('services', args = [request.user.id]))
    else:
        form=ScheduleForm()
    context={'form':form,'employee':employee, 'client':client}
    return render(request, 'schedule.html', context)

class UpdateSchedule(UpdateView):
    model = Services
    form_class = UpdateScheduleForm
    template_name = 'update_schedule.html'

    def get_success_url(self):
        return reverse('services', kwargs={'user_id': self.object.profile_id})

@login_required
def Budget(request, employee_id):
    employee = Employee.objects.get(user_id=employee_id)
    client = Client.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form=BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.value = form.cleaned_data['value']
            budget.client = client
            budget.employee = employee
            budget.save()
            return HttpResponseRedirect(reverse('schedule', args = [employee_id]))
    else:
        form=BudgetForm()
    context={'form':form,'employee':employee, 'client':client}
    return render(request, 'budget.html', context)

class UpdateBudget(UpdateView):
    model = Services
    form_class = UpdateBudgetForm
    template_name = 'update_budget.html'

    def get_success_url(self):
        return reverse('services', kwargs={'user_id': self.object.profile_id})