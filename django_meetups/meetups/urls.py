from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<slug:slug>', views.meetup_details, name='meetup-detail'),
]