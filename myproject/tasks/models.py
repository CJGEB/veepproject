from django.db import models
from boards.models import Item
from django.contrib.auth.models import User

# Create your models here.

class Media_Erasure (models.Model):
    item_nbr = models.ForeignKey(Item, on_delete = models.CASCADE, related_name='meadia_erasure')
    complete = models.BooleanField(default=0)
    complete_date = models.DateTimeField(auto_now_add = True)
    complete_by = models.ForeignKey(User, on_delete = models.CASCADE)

class Quality_Assessment (models.Model):
    item_nbr = models.ForeignKey(Item, on_delete=models.CASCADE)
    quality = models.CharField(max_length = 300)
    complete_date = models.DateTimeField(auto_now_add = True)
    complete_by = models.ForeignKey(User, on_delete = models.CASCADE)
    comments = models.CharField(max_length = 300, default=None)

class Parts_Harvesting (models.Model):
    item_nbr = models.ForeignKey(Item, on_delete=models.CASCADE)
    #TODO list of parts parts harvested
    complete_date = models.DateTimeField(auto_now_add=True)
    complete_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=300)

class Evaluation (models.Model):
    item_nbr = models.ForeignKey(Item, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    #TODO total_value = unit_price*Item.qty
    complete_date = models.DateTimeField(auto_now_add=True)
    complete_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=300, default=None)
