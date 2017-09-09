from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404

def index(request):
    if request.LANGUAGE_CODE =='zh-hans':
        return HttpResponse(request.LANGUAGE_CODE)
    else:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'TTapp/index.html', context)
        #return HttpResponse("You prefer to read another language.")

def TT_Site(request):
    if request.LANGUAGE_CODE =='zh-hans':
        return HttpResponse("This is TT site")
    else:
        return HttpResponse("You prefer to read another language. This is TT site")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'TTapp/detail.html', {'question': question})
    
    #Short cut of above code
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
