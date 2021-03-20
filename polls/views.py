from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    
    context = {
        "questions" : questions
    }

    return render(request, "polls/index.html", context)
    
def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question
    }

    return render(request, "polls/detail.html", context)



def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)

    for choice_pk in choices:
        choice = question.choice_set.get(pk=choice_pk)
        choice.votes += 1
        choice.save()

    return HttpResponseRedirect( reverse("polls:result", args=(q_id, )) )

def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question
    }

    return render(request, "polls/results.html", context)

def meme(request):
    return HttpResponse('<img src="https://n1s1.hsmedia.ru/c8/9f/cb/c89fcb31dd077084bc8bbc2284586b7f/1000x600_0xac120003_16946826431608901545.jpg" alt="notfound"> ')