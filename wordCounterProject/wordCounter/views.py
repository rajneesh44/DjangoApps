from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html',  {'hithere':'this is me'})
# 	return HttpResponse("Hello world")


