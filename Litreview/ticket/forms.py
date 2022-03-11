from django.forms import ModelForm, CharField, Textarea, IntegerField, ChoiceField
from . import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import PositiveSmallIntegerField, TextField


class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "rating", "body"]


class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


class TicketCritiqueForm(ModelForm):

    rating = ChoiceField(
        choices=[("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)]
    )
    headline = CharField()
    body = CharField(widget=Textarea)
    # rating = IntegerField(min_value=0, max_value=5)

    class Meta:
        model = models.Ticket
        fields = ("title", "description", "image")

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def save(self):
        self.instance.user = self.user
        ticket = super().save()
        review = models.Review(
            ticket=ticket,
            rating=self.cleaned_data["rating"],
            user=self.user,
            headline=self.cleaned_data["headline"],
            body=self.cleaned_data["body"],
        )
        review.save()
        return ticket


class ReviewUpdateForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline", "rating", "body"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        self.ticket = kwargs.pop("ticket")
        super().__init__(*args, **kwargs)

    def save(self):
        self.instance.ticket = self.ticket
        self.instance.user = self.user

        return super().save()
