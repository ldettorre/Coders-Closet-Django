# Generated by Django 2.0.7 on 2018-07-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('test', 'test item'), ('MENS_TSHIRTS', 'Mens T-Shirts'), ('MENS_JEANS', 'Mens Jeans'), ('MENS_SHOES', 'Mens Shoes')], default='test', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=254),
        ),
    ]
