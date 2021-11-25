from django.shortcuts import redirect, render
from .models import Meetup, Participant
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', { 'meetups': meetups })


def meetup_details(request, slug):
    selected_meetup = Meetup.objects.get(slug=slug)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get('email')
            participant, _ = Participant.objects.get_or_create(email=user_email)
            selected_meetup.participants.add(participant)
            messages.success(request, f'Your registration for { selected_meetup.title } is succeded!!')
            return redirect('all-meetups')
    else:
        form = RegistrationForm()
    return render(request, 'meetups/meetup-details.html', {'selected_meetup' : selected_meetup, 'form' : form})