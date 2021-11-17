from django.core.validators import slug_unicode_re
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price', )
    elif sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    else:
        phone_objects = Phone.objects.all()
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    context = {'phone': phone_objects[0]}
    return render(request, template, context)
