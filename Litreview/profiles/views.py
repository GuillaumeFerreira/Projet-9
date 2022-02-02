from django.shortcuts import render , redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, TemplateView
from . import forms

class LoginPageView(LoginView):

    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class HomeView(LoginRequiredMixin, TemplateView):

   template_name = 'header.html'


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'signup.html', context={'form': form})
