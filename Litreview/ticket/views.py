from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



class UpdateTicketViews(LoginRequiredMixin, UpdateView):

    model = models.Ticket
    fields = ["title", "description", "image"]
    template_name = "update_ticket.html"
    success_url = reverse_lazy("posts")
    template_name_suffix = "_update_form"


class UpdateReviewViews(LoginRequiredMixin, UpdateView):

    model = models.Review
    template_name = "update_review.html"
    success_url = reverse_lazy("posts")
    template_name_suffix = "_update_form"
    form_class = forms.ReviewUpdateForm


class CreateTicketViews(LoginRequiredMixin, CreateView):

    model = models.Ticket
    fields = ["title", "description", "image"]
    template_name = "create_ticket.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CreateReviewFromTicketViews(LoginRequiredMixin, CreateView):

    model = models.Review
    template_name = "create_Review_from_ticket.html"
    success_url = reverse_lazy("home")
    form_class = forms.ReviewCreateForm



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        self.ticket = models.Ticket.objects.get(id=self.kwargs["ticket_id"])
        kwargs["ticket"] = self.ticket
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticket"] = self.ticket
        return context


class CreateTicketReviewViews(LoginRequiredMixin, CreateView):

    model = models.Ticket
    template_name = "create_ticket_Review.html"
    success_url = reverse_lazy("home")
    form_class = forms.TicketCritiqueForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TicketDeleteView(DeleteView):

    model = models.Ticket
    success_url = reverse_lazy("posts")


class ReviewDeleteView(DeleteView):

    model = models.Review
    success_url = reverse_lazy("posts")
