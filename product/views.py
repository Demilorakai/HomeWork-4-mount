from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.


def homepage(request):
    products = Product.objects.all()
    context = {"all_vegetables": products}
    return render(request, "product_list.html", context)


def navar(request):
    tovary_object = Product.objects.get(id=1)
    description = tovary_object.description
    return HttpResponse(description, request)
