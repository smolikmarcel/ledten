from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, ProductsImg, ProductCategory
from .forms import form
from .filters import ProductsFilter, Filter


# Create your views here.

def produkty(request):
    products = Product.objects.all()
    filter = ProductsFilter(request.GET, queryset=products)

    paginator = Paginator(filter.qs, 40)
    page = request.GET.get('page')
    products = paginator.get_page(page)


    context = {
        "products": products,
        "productsImg": ProductsImg.objects.all().distinct('code'),
        "filter": filter,
        "form": form,
    }

    return render(request, 'produkty/produkty.html', context)

def produkty_f(request, category):
    products = ProductCategory.objects.all()
    filter = Filter(request.GET.get('category1'), queryset=products)

    paginator = Paginator(filter.qs, 40)
    page = request.GET.get('page')
    products = paginator.get_page(page)


    context = {
        "products": products,
        "productsImg": ProductsImg.objects.all().distinct('code'),
        "filter": filter,
        "form": form,
    }

    return render(request, 'produkty/produkty.html', context)



def produkt_detail(request, code):

    context = {
        "product": Product.objects.get(code=code),
        "productImgs": ProductsImg.objects.filter(code=code),
        "products": Product.objects.all()[:15],
        "productsImg": ProductsImg.objects.all().distinct('code')
    }

    return render(request, 'produkty/produkt_detail.html', context)
