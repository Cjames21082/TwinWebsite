from django.shortcuts import render, get_object_or_404
#from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from polls.models import Question, Choice

def home(request):
	return render(request, 'home.html')

def guess(request):
	return render(request, 'polls/whoamI.html')

# Original version
# def index(request):
# 	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
# 	context = {'latest_question_list': latest_question_list}
# 	return render(request, 'polls/index.html',context)

#Generic View
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		""" Return the last 5 published questions (Not including those
			set to be published in the future). """
		return Question.objects.filter(pub_date__lte = timezone.now()).\
			   										   order_by('-pub_date')[:5]

# Original version
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/details.html', {'question': question})

# Generic View
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/details.html'

	def get_queryset(self):
		""" Excludes any questions that aren't published yet """

		return Question.objects.filter(pub_date__lte=timezone.now())

# Original View
# def results(request, question_id):
# 	poll = get_object_or_404(Question, pk = question_id)
# 	return render(request, 'polls/results.html', {'poll': poll})

# Generic View
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = p.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the poll voting form
	    return render(request, 'polls/details.html', {
	    	'poll' : p,
	    	'error_message' : "You didn't select a choice.",
	    	})
 	else:	
	 	selected_choice.votes += 1
	 	selected_choice.save()
	 	# Always return an HttpResponseRedirect after successfully dealing
	    # with POST data. This prevents data from being posted twice if a
	    # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args = (p.id,)))


