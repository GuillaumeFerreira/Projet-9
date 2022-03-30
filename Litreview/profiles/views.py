from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, DeleteView, View, CreateView
from . import forms, models
from ticket.models import Ticket, Review
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, User
from django.forms import CharField, PasswordInput
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from itertools import chain


class LoginPageView(LoginView):

    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("home")


class LogoutPageView(LogoutView):

    next_page = reverse_lazy('login')




class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["followed_user"] = models.UserFollows.objects.filter(
            user=self.request.user
        )
        followed_users = []
        for follow in context["followed_user"]:
            followed_users.append(follow.followed_user)

        context["reviews"] = Review.objects.filter(user__in=followed_users).order_by(
            "time_created"
        )

        context["tickets"] = Ticket.objects.filter(user__in=followed_users).order_by(
            "time_created"
        )

        context["post"] = sorted(
            chain(context["reviews"], context["tickets"]),
            key=lambda post: post.time_created,
            reverse=True
        )

        return context



class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'signup.html'
  success_url = reverse_lazy('home')
  form_class = forms.SignupForm
  success_message = "%(username)s was created successfully"




class Followers(LoginRequiredMixin, FormView):

    template_name = "subscription.html"
    success_url = reverse_lazy("subscription")
    form_class = forms.FollowsForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FollowerDeleteView(DeleteView):
    model = models.UserFollows
    success_url = reverse_lazy("subscription")


class MyPostsView(LoginRequiredMixin, TemplateView):

    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(user=self.request.user).order_by(
            "time_created"
        )
        context["tickets"] = Ticket.objects.filter(user=self.request.user).order_by(
            "time_created"
        )
        return context
