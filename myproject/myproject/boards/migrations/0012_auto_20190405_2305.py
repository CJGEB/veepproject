# Generated by Django 2.1.5 on 2019-04-05 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0011_item_invoice_nbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='starter',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]
