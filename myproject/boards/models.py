from django.db import models

# Create your models here.

# below are copyed from the board project
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator

'''
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
'''

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
    '''
    # warehousenum = models.IntegerField(unique = True)
    # invoicenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    warehousenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    invoice_nbr = models.CharField(max_length = 10, default = 0)

    '''
    MANUFACTURER = (
    ('Apple', 'Apple'),
    ('Dell', 'Dell'),
    ('HP', 'HP'),
    ('MicroSoft', 'MicroSoft'),
    ('Lenovo', 'Lenovo'),
    ('Google', 'Google'),
    # ('')
    )
    '''
    manufacturer = models.CharField(max_length = 300) # , choices = MANUFACTURER)
    '''
    ITEM_TYPE = (
    ('Laptop', 'Laptop'),
    ('Desktop', 'Desktop'),
    ('Printer', 'Printer'),
    ('HardDrive', 'HardDrive'),
    # ('')
    )
    '''

    POWER_TEST = [('Yes', 'Pass.'),
    ('No', 'Fail.')]
    item_type = models.CharField(max_length = 200) # , choices = ITEM_TYPE)
    power_test = models.CharField(max_length=100, choices=POWER_TEST,default ='No')
    received_date = models.DateTimeField(auto_now_add = True)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, default=-1, related_name='items')
    invoice_nbr = models.ForeignKey(Donor, on_delete=models.CASCADE, default=-1, related_name='donor')


    def __str__(self):
        return self.warehousenum
    '''
    warehousenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    manufacturer = models.CharField(max_length = 300) # , choices = MANUFACTURER)
    item_model = models.CharField(max_length = 200)
    item_type = models.CharField(max_length = 200) # , choices = ITEM_TYPE)

    # recieved_date = models.DateTimeField(auto_now_add = True)

    # starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'items')

    starter = models.ForeignKey(User, on_delete=models.CASCADE, default=-1, related_name='items')
    invoice_nbr = models.ForeignKey(Donor, on_delete=models.CASCADE, default=-1, related_name='donor')

class Type(models.Model):
    # type_of_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'types')
    serialnum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    cpu_type = models.CharField(max_length = 200)
    speed = models.CharField(max_length = 200)
    memory_mb = models.CharField(max_length = 200)
    hd_size = models.CharField(max_length = 200)
    screen_size = models.CharField(max_length = 200)
    cd_type = models.CharField(max_length = 200)
    operating_system = models.CharField(max_length = 200)
    power_test = models.CharField(max_length = 100, default='--')

    # starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='types')
    warehouse_nbr = models.ForeignKey(Item, on_delete=models.CASCADE, default=-1, related_name='item' )

class Test(models.Model):
    POWER_TEST = (
        ('Y', 'Pass.'),
        ('N', 'Fail.')
    )
    power_test = models.CharField(max_length = 100, choices = POWER_TEST, default='--')
    tested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tests')

'''
class Evaluation(models.Model):
    # evaluation_stage = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_at = models.DateTimeField(auto_now_add = True)
'''

'''
class Type(models.Model).tables ?TABLE?:
    # type_of_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'types')
    model_of_item = models.CharField(max_length = 1000)
    attribute_name = models.CharField(max_length = 2000)


class Test(models.Model):
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

class Evaluation(models.Model):
    # evaluation_stage = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_at = models.DateTimeField(auto_now_add = True)
'''

