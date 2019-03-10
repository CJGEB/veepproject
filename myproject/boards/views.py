'''
from django.shortcuts import render

# Create your views here.

# recieve a request as a parameter, then return a responsea as a result
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to reBOOT Canada!')
'''
'''
# below, copyed from tutorial, with modification

from django.http import HttpResponse
from .models import Item

def home(request):
    items = Item.objects.all()
    item_names = list()

    for item in items:
        item_names.append(item.warehousenum)

    response_html = '<br>'.join(item_names)

    return HttpResponse(response_html)
'''
from django.shortcuts import render, get_object_or_404
# from .models import Item
from .models import Donor
from django.http import Http404

def home(request):
    donors = Donor.objects.all()
    return render(request, 'home.html', {'donors': donors})

def donations_info(request, pk):
    try:
        info = Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        raise Http404
    return render(request, 'donations_info.html', {'info': info})

def new_evaluation(request, pk):
    try:
        items = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404
    return render(request, 'new_evaluation.html', {'items': items})
