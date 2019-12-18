from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from django.shortcuts import render
from django.template import RequestContext

from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import User
 
def show_profile(request):
    return render(request, "profile.html")


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('profile.html')
    
    user_form = SignUpForm()
    profile_form = ProfileForm()
    return render(request, 'registration/signup.html',  
        {
            'user_form': user_form, 
            'profile_form': profile_form
        })



def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = UserProfile()
        profile.user = user
        profile.save()

post_save.connect(create_profile, sender=User)