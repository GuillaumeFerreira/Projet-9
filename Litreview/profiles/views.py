from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, DeleteView, CreateView
from . import forms, models
from ticket.models import Ticket, Review
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from itertools import chain


class LoginPageView(LoginView):

    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("home")


class LogoutPageView(LogoutView):

    next_page = reverse_lazy("login")


class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        followed_users = models.UserFollows.objects.filter(
            user=self.request.user
        ).values_list("followed_user_id", flat=True)

        reviews = Review.objects.filter(user__in=followed_users).order_by(
            "time_created"
        )

        tickets = Ticket.objects.filter(user__in=followed_users).order_by(
            "time_created"
        )
        tickets_user = Ticket.objects.filter(user=self.request.user).order_by(
            "time_created"
        )
        reviews_user = Review.objects.filter(user=self.request.user).order_by(
            "time_created"
        )
        context["posts"] = sorted(
            chain(reviews, tickets, tickets_user, reviews_user),
            key=lambda post: post.time_created,
            reverse=True,
        )
        context["ticket_id_review"] = Review.objects.values_list("ticket_id", flat=True)

        return context


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "signup.html"
    success_url = reverse_lazy("home")
    form_class = forms.SignupForm
    success_message = "%(username) a été créé avec succès"


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
