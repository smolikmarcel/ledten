# Generated by Django 2.1.4 on 2019-03-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0009_auto_20190311_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='category',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]