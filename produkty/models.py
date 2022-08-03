from django.db import models
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=30, blank=True, unique=True, null=True)
    jmeno = models.CharField(max_length=250, blank=True)

    guide = models.CharField(max_length=250, blank=True, unique=True)

    shortDescription = models.TextField(blank=True)
    description = models.TextField(blank=True)

    vyrobce = models.CharField(max_length=30)

    zasoby = models.BigIntegerField(default=0, null=True)
    cena = models.BigIntegerField(default=100, null=True)


    def __str__(self):
        return self.code

    def card(self):
        return self.jmeno[:65]




class ProductsImg(models.Model):
    code = models.CharField(max_length=30, blank=True)
    img = models.ImageField(default='default_bulb.jpg', blank=True)



class ProductCategory(models.Model):
    CHOICES = (
        ('LED žárovky', 'LED žárovky'),
        ('LED reflektory', 'LED reflektory'),
        ('LED svítidla RGB', 'LED svítidla RGB'),
        ('LED pásky + příslušenství', 'LED pásky + příslušenství'),
        ('LED reflektory s čidlem pohybu', 'LED reflektory s čidlem pohybu'),
        ('LED svítidla vnitřní', 'LED svítidla vnitřní'),
        ('LED Trubice', 'LED Trubice'),
        ('LED reflektory RGB', 'LED reflektory RGB'),
        ('přenosný reflektor', 'přenosný reflektor'),
        ('příslušenství', 'příslušenství'),
        ('Redukce', 'Redukce'),
        ('stropní', 'stropní'),
        ('zoom profesional', 'zoom profesional'),
        ('ČIDLA POHYBU', 'ČIDLA POHYBU'),
        ('RETRO', 'RETRO'),
        ('SADY', 'SADY'),
        ('SLIM', 'SLIM'),
        ('100W', '100W'),
        ('70W', '70W'),
        ('30W', '30W'),
        ('20W', '20W'),
        ('18W', '18W'),
        ('15W', '15W'),
        ('12W', '12W'),
        ('10W', '10W'),
        ('8W', '8W'),
        ('7W', '7W'),
        ('6W', '6W'),
        ('5W', '5W'),
        ('4W', '4W'),
        ('3W', '3W'),
        ('2,5W', '2,5W'),
        ('2W', '2W'),
        ('1,5W', '1,5W'),
        ('1,2W', '1,2W'),
        ('1W', '1W'),
        ('E14', 'E14'),
        ('E27', 'E27'),
        ('GU10', 'GU10'),
        ('G9', 'G9'),
        ('GU5,3', 'GU5,3'),
        ('G4', 'G4'),
        ('IP 65', 'IP 65'),
        ('IP 20', 'IP 20'),
        ('120cm', '120cm'),
        ('60cm', '60cm'),
    )

    code = models.ForeignKey(Product, on_delete=models.PROTECT, default=1)
    #category = models.CharField(max_length=250, blank=True, choices = CHOICES)
    category = MultiSelectField(choices = CHOICES)

    def __str__(self):
        return self.code.code
