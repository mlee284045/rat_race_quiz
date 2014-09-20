from django import forms
from django.contrib.auth.forms import UserCreationForm
from rat_race.models import Runner


class RunnerForm(UserCreationForm):

    class Meta:
        model = Runner
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]