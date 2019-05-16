from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from adviseMeApp.models import Topic, Comment

# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Profile(generic.DetailView):
    template_name = 'registration/profile.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Topic.objects.filter(user=self.request.user.id)


    def get_object(self):
        return self.request.user


