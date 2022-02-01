from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView, TemplateView
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginPageView(LoginView):

    template_name = 'base/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('home')


class LoginPageView_old(View):
    template_name = 'base/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})


class TicketCreateView(CreateView):

    form_class = forms.TicketForm
    sucess_url = reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class HomeView(LoginRequiredMixin, TemplateView):

   template_name = 'base/home.html'

@login_required
def home(request):
    return render(request, 'base/home.html')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'base/signup.html', context={'form': form})


def flux(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def subscriptions(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def create_ticket(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def create_review(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def post(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def to_modify_review(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def to_modify_ticket(request):
    return HttpResponse('<h1>Hello Django!</h1>')
