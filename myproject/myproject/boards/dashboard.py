from controlcenter import Dashboard, widgets
from project.app.models import Model

class ModelItemList(widgets.ItemList):
    model = Model
    list_display = ('pk', 'field')

class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )
    
