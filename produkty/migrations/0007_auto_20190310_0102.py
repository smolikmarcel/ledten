# Generated by Django 2.1.4 on 2019-03-10 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0006_remove_productcategory_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='cod',
            new_name='code',
        ),
    ]
