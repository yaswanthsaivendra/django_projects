from django.shortcuts import render
from .models import Meetup

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', { 'meetups': meetups })


def meetup_details(request, slug):
    selected_meetup = Meetup.objects.get(slug=slug)
    return render(request, 'meetups/meetup-details.html', {'selected_meetup' : selected_meetup})