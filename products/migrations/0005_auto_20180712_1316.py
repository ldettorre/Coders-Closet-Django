# Generated by Django 2.0.7 on 2018-07-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_merge_20180709_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MENS_TSHIRTS', 'Mens T-Shirts'), ('MENS_JEANS', 'Mens Jeans'), ('MENS_SHOES', 'Mens Shoes')], default='MENS_TSHIRTS', max_length=30),
        ),
    ]