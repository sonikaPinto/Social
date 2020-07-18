from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView
from accounts.forms import UserForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
    form_class = UserForm
    model = get_user_model
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signUp.html'
