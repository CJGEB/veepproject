from django.contrib import admin

# Register your models here.

# from .models import Item
from .models import Donor, Item, Type


# @admin.site.register(Donor)
@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['donorname', 'invoicenum', 'number_of_donations', 'last_updated']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'item_type', 'item_model']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['serialnum', 'serialnum', 'operating_system']
