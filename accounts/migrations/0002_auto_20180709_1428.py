# Generated by Django 2.0.7 on 2018-07-09 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='user',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]