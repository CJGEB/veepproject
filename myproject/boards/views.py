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

from .models import Donor, Item
from tasks.models import Media_Erasure
from django.http import Http404
from django.contrib.auth.models import User


def home(request):
    donors = Donor.objects.all()
    return render(request, 'home.html', {'donors': donors})




def donationsinfo(request, pk):
    try:
        items = Donor.objects.get(pk=pk)
    except Donor.DoesNotExist:
        raise Http404
    return render(request, 'donationsinfo.html', {'items': items})



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
        power_test = request.POST['power_test']

        user = request.user

        item = Item.objects.create(
            warehousenum=warehousenum,
            # donations=donations,
            item_type=item_type,
            manufacturer=manufacturer,
            power_test=power_test,
            starter=user
        )

        media_erasure = Media_Erasure.objects.create(

            item_nbr = item,
            complete_by = user
        )


        return redirect('donationsinfo', pk=donations.pk)
    return render(request, 'new_donations.html', {'donations': donations})


'''
        evaluation = Evaluation.objects.create(

            evaluated_by=user

        )
'''
