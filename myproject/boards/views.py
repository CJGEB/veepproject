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
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Item
from .models import Donor, Item, Test, Evaluation
from django.http import Http404
from django.contrib.auth.models import User

def home(request):
    donors = Donor.objects.all()
    return render(request, 'home.html', {'donors': donors})

def donationsinfo(request, pk):
    try:
        info = Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        raise Http404
    return render(request, 'donationsinfo.html', {'info': info})

def new_donations(request, pk):
    '''
    try:
        donations = Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        raise Http404
    return render(request, 'new_donations.html', {'donations': donations})
    '''
    donations = get_object_or_404(Donor, pk=pk)

    if request.method == 'POST':
        warehousenum = request.POST['warehousenum']
        item_type = request.POST['item_type']
        manufacturer = request.POST['manufacturer']

        user = User.objects.first()  # TODO: get the currently logged in user

        item = Item.objects.create(
            warehousenum=warehousenum,
            # donations=donations,
            item_type=item_type,
            manufacturer=manufacturer,
            # starter=user
        )
        '''
        evaluation = Evaluation.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        '''

        return redirect('donationsinfo', pk=donors.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_donations.html', {'donations': donations})
