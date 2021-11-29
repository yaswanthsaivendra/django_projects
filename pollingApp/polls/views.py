from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from polls.forms import QuestionForm
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = QuestionForm()

    return render(request, 'polls/detail.html', {'question' : question, 'form' : form})

def results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
