from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
# Create your views here.
def homePage(request):
    return render(request, 'index.html')
def mens_products(request):
    products = Product.objects.filter(category='Men')
    return render(request, 'mens.html', {'products': products})
def womens_products(request):
    products = Product.objects.filter(category='Women')
    return render(request, 'womens.html', {'products': products})
def tanktop_products(request):
    products = Product.objects.filter(category='Tank Top')
    return render(request, 'tanktop.html', {'products': products})
def swimwear_products(request):
    products = Product.objects.filter(category='Swimwear')
    return render(request, 'swimwear.html', {'products': products})
def sundress_products(request):
    products = Product.objects.filter(category='Sundress')
    return render(request, 'sundress.html', {'products': products})
def bright_products(request):
    products = Product.objects.filter(category='Bright')
    return render(request, 'bright.html', {'products': products})
def heavycoat_products(request):
    products = Product.objects.filter(category='Heavy Coat')
    return render(request, 'heavycoat.html', {'products': products})
def gloves_products(request):
    products = Product.objects.filter(category='Gloves')
    return render(request, 'gloves.html', {'products': products})
def hats_products(request):
    products = Product.objects.filter(category='Hats')
    return render(request, 'hats.html', {'products': products})
def thermal_products(request):
    products = Product.objects.filter(category='Thermal')
    return render(request, 'thermal.html', {'products': products})
def longsleeves_products(request):
    products = Product.objects.filter(category='Long Sleeves')
    return render(request, 'longsleeves.html', {'products': products})
def sweaters_products(request):
    products = Product.objects.filter(category='Sweaters')
    return render(request, 'sweaters.html', {'products': products})
def jeans_products(request):
    products = Product.objects.filter(category='Jeans')
    return render(request, 'jeans.html', {'products': products})
def fall_products(request):
    categories = ['Long Sleeves', 'Sweaters', 'Jeans']
    products = Product.objects.filter(category__in=categories)
    return render(request, 'fall.html', {'products': products})
def summer_products(request):
    categories = ['Tank Top', 'Sundress', 'Swimwear', 'Bright']
    products = Product.objects.filter(category__in=categories)
    return render(request, 'summer.html', {'products': products})
def winter_products(request):
    categories = ['Heavy Coat', 'Gloves', 'Hats', 'Thermal']
    products = Product.objects.filter(category__in=categories)
    return render(request, 'winter.html', {'products': products})