from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from django.shortcuts import render
from django.template import RequestContext

from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *

 
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
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'registration/signup.html',  context_instance=RequestContext(request))
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
        return render(request, 'registration/signup.html',  
            {
                'user_form': user_form, 
                'profile_form': profile_form
            })
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()


