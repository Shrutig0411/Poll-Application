from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Polls/index.html'
    context_object_name = 'recently_added_ques'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'Polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'Polls/results.html'

def vote(request, ques_id):
    question = get_object_or_404(Question, pk=ques_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Polls:results', args=(question.id,)))