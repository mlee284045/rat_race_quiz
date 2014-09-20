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
            runner = form.save()
            runner.email_user('Welcome to the Rat Race', 'Thanks for joining. Will you be able to last till the end? We shall see...', settings.DEFAULT_FROM_EMAIL)

            return redirect('home')
    else:
        form = RunnerForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    runner = Runner.objects.get(id=request.user.id)
    data = {'long': runner.location_long, 'lat': runner.location_lat}
    # data = {'user': request.user}
    return render(request, 'profile.html', data)

