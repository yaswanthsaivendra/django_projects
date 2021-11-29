from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CreatePollForm
from .models import Poll
# Create your views here.

def index(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/index.html',context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else :
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'polls/create.html',context)

def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else :
            return HttpResponse(400, ' Invalid Form ')
        poll.save()
        return redirect('polls:results', poll.id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/vote.html',context)

def results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/results.html',context)


