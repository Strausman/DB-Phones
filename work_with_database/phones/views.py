from django.shortcuts import render, redirect
from django.http import HttpResponse

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    all_phones = Phone.objects.all()

    if sort_pages == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'name':
        phones = all_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': all_phones}
    return render(request, template, context)

    # sort_by = request.GET.get('sort', 'name')
    # if sort_by == 'name':
    #     phones = Phone.objects.all().order_by('name')
    # elif sort_by == 'price_asc':
    #     phones = Phone.objects.all().order_by('price')
    # elif sort_by == 'price_desc':
    #     phones = Phone.objects.all().order_by('-price')
    # else:
    #     phones = Phone.objects.all()
    #
    # return render(request, 'catalog.html', {'phones':phones})


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phones': phones}
    return render(request, template, context)
    # phone = get_object_or_404(Phone, slug=slug)
    # template = 'product.html'
    # context = {}
    # return render(request, 'product.html', {'phone': phone})
