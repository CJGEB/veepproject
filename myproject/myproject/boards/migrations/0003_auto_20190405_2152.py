# Generated by Django 2.1.5 on 2019-04-05 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190405_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='invoice_nbr',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='boards.Donor'),
        ),
        migrations.AlterField(
            model_name='type',
            name='warehouse_nbr',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='boards.Item'),
        ),
    ]