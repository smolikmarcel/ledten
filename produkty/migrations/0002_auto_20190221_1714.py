# Generated by Django 2.1.4 on 2019-02-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsimg',
            name='code',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
