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
import random
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Item
from .models import Donor, Item, Type, Evaluation
from django.http import Http404
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    donors = Donor.objects.all()
    return render(request, 'home.html', {'donors': donors})

def donationsinfo(request, pk):
    '''
    try:
        items = Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        raise Http404
    return render(request, 'donationsinfo.html', {'items': items})
    '''
    try:
        invoice = Donor.objects.get(pk=pk)
        items = Item.objects.filter(invoice_nbr=invoice)
        ware = Item.objects.get(pk=pk)
        types = Type.objects.filter(warehouse_nbr=ware)
    except Donor.DoesNotExist:
        raise Http404
    return render(request, 'donationsinfo.html', {'items': items, 'invoice':invoice, 'ware': ware, 'types': types})



def new_donations(request, pk):

    donations = get_object_or_404(Donor, pk=pk)
    ware = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':

        warehousenum = request.POST['warehousenum']
        '''
        warehousenum = User.objects.make_random_password(length=10, allowed_chars='123456789')
        while User.objects.filter(userprofile__temp_password=random_number):
            random_number = User.objects.make_random_password(length=10, allowed_chars='123456789')
        '''
        item_type = request.POST['item_type']
        manufacturer = request.POST['manufacturer']
        item_model = request.POST['model']


        power_test = request.POST['power_test']
        serialnum = request.POST['serialnum']
        cpu_type = request.POST['cpu_type']
        speed = request.POST['speed']
        memory_mb = request.POST['memory_mb']
        hd_size = request.POST['hd_size']
        screen_size = request.POST['screen_size']
        cd_type = request.POST['cd_type']
        operating_system = request.POST['operating_system']

        user = request.user

        item = Item.objects.create(
            warehousenum = warehousenum,
            item_model = item_model,
            item_type = item_type,
            manufacturer = manufacturer,
            starter = user,
            invoice_nbr = donations
        )

        type = Type.objects.create(
            serialnum = serialnum,
            cpu_type = cpu_type,
            speed = speed,
            memory_mb = memory_mb,
            hd_size = hd_size,
            screen_size = screen_size,
            cd_type = cd_type,
            operating_system = operating_system,
            power_test = power_test,
            warehouse_nbr = item
        )

        return redirect('donationsinfo', pk=donations.pk)
    return render(request, 'new_donations.html', {'donations': donations})

def detail_info(request, pk):
    '''
    detailinfo = Type.objects.get(pk=pk)
    return render(request, 'detail_info.html', {'detailinfo': detailinfo})

    '''
    try:
        ware = Item.objects.get(pk=pk)
        types = Type.objects.filter(warehouse_nbr=ware)
    except Donor.DoesNotExist:
        raise Http404
    # return HttpResponse(types)
    return render(request, 'detail_info.html', {'types': types, 'ware':ware})
