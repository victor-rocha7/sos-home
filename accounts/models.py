from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from pages.models import Category


class User(AbstractUser):
    is_client = models.BooleanField('É cliente', default=False)
    is_employee = models.BooleanField('É prestador', default=False)
    
    name = models.CharField('Nome Completo', max_length=255)
    email = models.CharField('E-mail', max_length=255)
    cpf = models.CharField('CPF', max_length=14)
    birth_date = models.DateField('Data de Nascimento', auto_now_add=True)
    gender = models.CharField('Sexo', max_length=30)
    adress = models.CharField('Endereço', max_length=255)
    imageURL = models.URLField('URL da Foto de Perfil', blank=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #exclusive fields: (NONE)
    
    def __str__(self):
        return self.user.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #exclusive fields: 
    available = models.CharField('Disponibilidade', max_length=255, blank=True, default='Nenhuma')
    job = models.ManyToManyField(Category)

    def __str__(self):
        return self.user.name

