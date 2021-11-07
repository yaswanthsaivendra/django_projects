from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'location' : 'New York',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'location' : 'New Delhi',
            'slug': 'a-second-meetup'
        },
    ]
    return render(request, 'meetups/index.html', { 'meetups': meetups })


def meetup_details(request, slug):
    selected_meetup = {
        'title' : 'A First Meetup',
        'description' : 'THis is a First Meetup'
    }
    return render(request, 'meetups/meetup-details.html', {'selected_meetup' : selected_meetup})