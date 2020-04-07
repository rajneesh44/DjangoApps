from django.shortcuts import render
from .models import Item
# Create your views here.


def moviePage(request):
    allItems = Item.objects.all()
    context = {'allitems':allItems}
    return render(request, 'movie/moviePage.html', context)