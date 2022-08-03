from django import forms
from .models import ProductCategory

class form(forms.Form):
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

    category = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = ProductCategory
        fields = ['category']
