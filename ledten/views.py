from django.shortcuts import render
from produkty.models import Product, ProductsImg


def homepage(request):
    context = {
        "products": Product.objects.all()[:8],
        "productsImg": ProductsImg.objects.all().distinct('code')
    }

    return render(request, 'homepage.html', context)

def proc_led(request):
    context = {
        "products": Product.objects.all()[:8],
        "productsImg": ProductsImg.objects.all().distinct('code')
    }

    return render(request, 'proc_led.html', context)

def kontakt(request):
    return render(request, 'kontakt.html')

def order(request):
    return render(request, 'order.html')
