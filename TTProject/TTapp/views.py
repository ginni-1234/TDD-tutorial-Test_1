from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    if request.LANGUAGE_CODE =='zh-hans':
        return HttpResponse(request.LANGUAGE_CODE)
    else:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('TTapp/index.html')
        context = {
        'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))
        #return HttpResponse("You prefer to read another language.")

def TT_Site(request):
    if request.LANGUAGE_CODE =='zh-hans':
        return HttpResponse("This is TT site")
    else:
        return HttpResponse("You prefer to read another language. This is TT site")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
