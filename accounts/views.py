from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView
from .forms import ClientSignUpForm, EmployeeSignUpForm
from .models import User, Employee, Client
from django.contrib import messages

def signup(request):
    return render(request, 'registration/signup_choice.html')

class ClientSignUp(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_client.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class EmployeeSignUp(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_employee.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def DetailEmployee(request, user_id):
    user = User.objects.get(id=user_id)
    employee = Employee.objects.get(user_id=user_id)
    temp_user = user
    if user.is_employee:
        temp_user.job = employee.job
        temp_user.available = employee.available
        context = {'employee': temp_user}
        return render(request, 'registration/detail_employee.html', context)

class UserUpdate(UpdateView):
    model = User
    template_name = 'registration/update_user.html'
    fields = ['name', 'adress', 'imageURL']
    success_url = reverse_lazy('user-profile')

    def get_object(self, queryset=None):
        user = User.objects.filter(pk=self.request.user.id).first()
        return user

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Meus dados pessoais'
        context['botao'] = 'Atualizar'
        
        return context

class Profile(CreateView):
    model = User
    fields = '__all__'
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        user = user.objects.filter(pk=self.request.user.id).first()
        return user

