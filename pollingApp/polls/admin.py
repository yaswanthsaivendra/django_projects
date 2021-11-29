from django.contrib import admin
from .models import Poll
from django.contrib.admin import ModelAdmin

# Register your models here.

class PollAdmin(ModelAdmin):
    list_display = ['id', 'question']

admin.site.register(Poll, PollAdmin)
