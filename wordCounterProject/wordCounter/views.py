from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
# 	return HttpResponse("Hello world")


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    wordcount={}
    for word in wordlist:
        if word in wordcount:
            #increase
            wordcount[word]+=1
        else:
            #add to dictionary
            wordcount[word]=1

    return render(request, 'Count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordcount': wordcount.items()})

