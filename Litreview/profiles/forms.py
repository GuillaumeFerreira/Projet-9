from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, ValidationError, Form
from . import models
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username",)


class FollowsForm(Form):

    # followed_user = CharField(label='')
    search_user = CharField(label="")

    # class Meta:
    # model = models.UserFollows
    # fields = ['followed_user']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        # self.followed_user = kwargs["followed_user"]

        super().__init__(*args, **kwargs)

    def save(self):

        user_follow = models.UserFollows.objects.create(
            user=self.user, followed_user=self.cleaned_data["search_user"]
        )

        # self.instance.user = self.user
        # self.instance.followed_user = self.cleaned_data['search_user']

        # followed_user = super().save()

        return user_follow

    def clean_search_user(self):

        search = self.cleaned_data["search_user"]
        User = get_user_model()
        if not User.objects.filter(username=search).exists():
            raise ValidationError("user not found")
        else:

            self.cleaned_data["search_user"] = User.objects.get(username=search)

        return self.cleaned_data["search_user"]
