from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, ValidationError, Form
from . import models
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
        ]


class FollowsForm(Form):

    search_user = CharField(label="")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def save(self):

        user_follow = models.UserFollows.objects.create(
            user=self.user, followed_user=self.cleaned_data["search_user"]
        )
        return user_follow

    def clean_search_user(self):

        search = self.cleaned_data["search_user"]
        User = get_user_model()
        if not User.objects.filter(username=search).exists():
            raise ValidationError("L'utilisateur n'existe pas")
        elif User.objects.filter(username=search)[0] == self.user:
            raise ValidationError("Vous ne pouvez pas être abonner à vous même")
        else:

            self.cleaned_data["search_user"] = User.objects.get(username=search)
            if models.UserFollows.objects.filter(
                followed_user=self.cleaned_data["search_user"]
            ).exists():
                raise ValidationError("Utilisateur déjà abonné")

        return self.cleaned_data["search_user"]
