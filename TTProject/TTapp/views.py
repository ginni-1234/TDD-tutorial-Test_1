from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.LANGUAGE_CODE =='zh-hans':
        return HttpResponse(request.LANGUAGE_CODE)
    else:
        return HttpResponse("You prefer to read another language.")
