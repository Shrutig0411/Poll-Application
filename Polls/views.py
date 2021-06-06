from django.shortcuts import get_object_or_404, render
from .models import Question
from django.template import loader
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def index(request):
    recently_added_ques=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('Polls/index.html')
    context = {
        'recently_added_ques': recently_added_ques,
    }
    return render(request, 'Polls/index.html', context)


def detail(request,ques_id):
    question=get_object_or_404(Question, pk=ques_id)
    return render(request, 'Polls/details.html', {'question': question}) 

def results(request,ques_id):
    return HttpResponse("You are looking at results for question %s." % ques_id) 

def vote(request,ques_id):
    return HttpResponse("You are voting on question %s." % ques_id)     
