# Generated by Django 2.1.5 on 2019-04-06 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_auto_20190405_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='warehouse_nbr',
            field=models.ForeignKey(default=3432423, on_delete=django.db.models.deletion.CASCADE, related_name='donor', to='boards.Item'),
            preserve_default=False,
        ),
    ]
