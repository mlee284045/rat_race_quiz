from django.shortcuts import render, redirect
from first_rocket import settings
from rat_race.forms import RunnerForm
from rat_race.models import Runner
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RunnerForm(request.POST)
        if form.is_valid():
            runner = Runner.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )
            runner.email_user('Welcome to the Rat Race', 'Thanks for joining. Will you be able to last till the end? We shall see...', settings.DEFAULT_FROM_EMAIL)

            return redirect('home')
    else:
        form = RunnerForm()
    return render(request, 'registration/register.html', {'form': form})


