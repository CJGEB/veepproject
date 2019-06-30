from django.db import models

# Create your models here.

# below are copyed from the board project
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator


class Donor(models.Model):
    # this should be a one-to-many field (i think), have no idea if it's possible...
    donorname = models.CharField(max_length = 200)
    # invoicenum = models.CharField(max_length = 200)
    invoicenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False, default = '2019')
    number_of_donations = models.IntegerField(default = 1)
    donor_email = models.CharField(max_length = 1000)
    # donor_phone = models.IntegerField(unique = True)
    donor_phone = models.CharField(max_length = 100)
    donor_address = models.CharField(max_length = 2000)
    last_updated = models.DateTimeField(auto_now_add = True)
    #item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'item')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'donors')


class Item(models.Model):
    # warehousenum = models.IntegerField(unique = True)
    # invoicenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    warehousenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    invoice_nbr = models.CharField(max_length = 10, default = 0)

    
    
    manufacturer = models.CharField(max_length = 300) # , choices = MANUFACTURER)
    
    

    POWER_TEST = [('Yes', 'Pass.'),
    ('No', 'Fail.')]
    item_type = models.CharField(max_length = 200) # , choices = ITEM_TYPE)
    power_test = models.CharField(max_length=100, choices=POWER_TEST,default =None)
    received_date = models.DateTimeField(auto_now_add = True)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, default=-1, related_name='items')
    invoice_nbr = models.ForeignKey(Donor, on_delete=models.CASCADE, default=-1, related_name='donor')


    def __str__(self):
        return self.warehousenum



class Type(models.Model):
    # type_of_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'types')
    model_of_item = models.CharField(max_length = 1000)
    attribute_name = models.CharField(max_length = 2000)


'''class Test(models.Model):
=======
class Test(models.Model):
>>>>>>> 734fa61af771c94121a265cc4894f5f5d443cc9e
    POWER_TEST = (
        ('Y', 'Pass.'),
    )
        ('N', 'Fail.')
<<<<<<< HEAD

    power_test = models.CharField(max_length = 100, choices = POWER_TEST, default='--')
    tested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tests')
'''
'''class Evaluation(models.Model):
    # evaluation_stage = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_at = models.DateTimeField(auto_now_add = True)
'''