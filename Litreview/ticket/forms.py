from django.forms import ModelForm, CharField, Textarea, ChoiceField, RadioSelect
from . import models


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


class ReviewCreateForm(ModelForm):

    rating = ChoiceField(
        choices=[("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)],
        widget=RadioSelect)

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

class ReviewUpdateForm(ModelForm):

    rating = ChoiceField(
        choices=[("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)],
        widget=RadioSelect)

    class Meta:
        model = models.Review
        fields = ["headline", "rating", "body"]

