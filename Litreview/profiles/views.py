from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, DeleteView, View
from . import forms, models
from ticket.models import Ticket, Review
from django.urls import reverse_lazy


class LoginPageView(LoginView):

    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("home")


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login")



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

        return context


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "signup.html", context={"form": form})


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
