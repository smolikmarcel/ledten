# Generated by Django 2.1.4 on 2019-03-10 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0005_productcategory_cod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='code',
        ),
    ]