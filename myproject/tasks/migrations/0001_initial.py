# Generated by Django 2.1.4 on 2019-04-04 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('complete_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(default=None, max_length=300)),
                ('complete_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Media_Erasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=0)),
                ('complete_date', models.DateTimeField(auto_now_add=True)),
                ('complete_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meadia_erasure', to='boards.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Parts_Harvesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(max_length=300)),
                ('complete_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Quality_Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=300)),
                ('complete_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(default=None, max_length=300)),
                ('complete_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_nbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('item_br', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Item')),
            ],
        ),
    ]
