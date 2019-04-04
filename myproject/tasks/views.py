from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from .status import *
from boards.models import Donor

def index(request):
    return HttpResponse('Hello %s, Here are your tasks for today' % request.user.get_short_name())


#navigate through various tasks pages
def task_option(request, option):
    if option == 'Evaluation':
        active = Evaluation.objects.filter(complete_by__isnull=False)
    elif option == 'Media Erasure':
        active = Media_Erasure.objects.filter(complete__exact=0)
    elif option == 'Parts Harvesting':
        active = Parts_Harvesting.objects.filter(complete_by__isnull=False)
    elif option == 'Quality Assessment':
        active = Quality_Assessment.objects.filter(complete_by__isnull=False)
    else:
        return render(request, 'tax_receipt.html')

    return render(request, 'task_list.html', {'option': option, 'active_tasks': active})


#homepage for all tasks
def main_tasks_page(request):
    tasks_list = ['Media Erasure',
                  'Quality Assessment',
                  'Parts Harvesting',
                  'Evaluation',
                  'Tax Receipt Generation'] #TODO can be adjusted based on user permission
    return render(request, 'tasks.html', {'tasks_list': tasks_list})


def task_forms(request, option, task):
    if option == 'Evaluation':
        return evaluation(request, task)
    elif option == 'Media Erasure':
        return mediaErasure(request, task)
    elif option == 'Parts Harvesting':
        return partsHarvesting(request, task)
    elif option == 'Quality Assessment':
        return qualityAsssesment(request, task)
    else:
        # TODO
        return HttpResponse('Tax Receipt Generation')



#Below are the forms to fill out when user complete tasks
def mediaErasure(request, task):



    #TODO initiate Quality Assessment; see boards/views - new donation for reference
    #qa = Quality_Assessment.objects.create(
    #   #fill in fields here
    #)

    updateStatus(Item, 'media erasure')

    return render(request, 'MEForms.html', {'task': task})

def qualityAsssesment(request, item_nbr):

    #TODO initiate Parts Harvesting model; see boards/views - new donation for reference
    #TODO initiate Evaluation model; see boards/views - new donation for reference

    updateStatus(Item, 'qualtify assessment')
    return None


def evaluation(request, item_nbr):
    return None

    updateStatus(Item, 'complete')

def taxReceipt(request):
    return None


def partsHarvesting(request):
    return None

    updateStatus(Item, 'qualtify assessment')
