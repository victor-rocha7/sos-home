from django import forms
from django.forms import ModelForm
from .models import Services
from django.contrib.admin import widgets


class ScheduleForm(forms.ModelForm):
    job_date_time = forms.DateTimeField(label='Data do serviço', widget=widgets.AdminSplitDateTime(attrs={'class': 'form-control'}))

    class Meta:
        model = Services
        fields = ('job_date_time',)

class BudgetForm(forms.ModelForm):
    budget = forms.IntegerField(label='Valor do orçamento', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Services
        fields = ('budget',)

class UpdateScheduleForm(forms.ModelForm):
    job_date = forms.DateTimeField(label='Data do serviço', required=True)
    
    class Meta:
        model = Services
        fields = ('job_date',)

class UpdateBudgetForm(forms.ModelForm):
    budget = forms.IntegerField(label='Valor do orçamento', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Services
        fields = ('budget',)