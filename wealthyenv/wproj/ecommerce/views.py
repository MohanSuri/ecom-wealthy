from django.shortcuts import render

# Create your views here.from django.shortcuts import render

from django.http import HttpResponse
#from .models import Question
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render


def index(request):
    return HttpResponse("Rest working")



''''
def index(request, question_id):


    #template=loader.get_template('ecommerce/index.html')
    #latest_question_list=Question.objects.all()
    question = get_object_or_404(Question, pk=question_id)
    context = {'latest_question_list': latest_question_list}
    #context= RequestContext(request,{'latest_question_list':latest_question_list})
    #return HttpResponse(template.render(context))
    return render(request, 'ecommerce/index.html', {'question': question})

def detail(request, question_id):
	return HttpResponse("You are looking at a question .")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ecommerce/results.html', {'question': question})

def vote(request, question_id):
	return HttpResponse("You are voting for this question %s" % question_id)

'''

