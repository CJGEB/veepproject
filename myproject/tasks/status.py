from .models import *

#update status to the next stage of the process;
#process order: initiate donation -> media erasure -> quality assessment -> parts harvesting -> evaluation -> complete

def updateStatus(item_nbr, option):
    if option == 'initial':
        Transaction.object.create(
            item_nbr = item_nbr.pk,
            status = 'media erasure'
        )
    elif option == 'media erasure':
        Transaction.objects.filter(item_nbr=item_nbr).update(status=='quality assessment')
    elif option == 'parts harvesting':
        #optional step; initiated by specifying parts harvesting
        Transaction.objects.filter(item_nbr=item_nbr.pk).update(status=='parts harvesting')
    elif option == 'quality assessment':
        Transaction.objects.filter(item_nbr=item_nbr.pk).update(status=='evaluation')
    else:
        Transaction.objects.filter(item_nbr=item_nbr.pk).update(status == 'complete')

    return True

def receiptStatus(request, invoice):
    #pseudo
    #update stat to incomplete if any one of the item in invoice is not complete (finished evaluation)
    stat = 'complete'
    for i in invoice:
        if i.item_nbr.status != 'complete':
            stat = 'in progress'
            break
        else:
            continue

    return stat

