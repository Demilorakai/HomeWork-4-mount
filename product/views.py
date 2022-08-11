from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Categories, Pricing
from .forms import RegistrationForm

# Create your views here.


def homepage(request):
    products = Product.objects.all()
    context = {"all_vegetables": products}
    return render(request, "product/product_list.html", context)


def category(request):
    categories = Categories.objects.all()
    context = {"categories": categories}
    return render(request, "product/categori.html", context)


def categories_info(request, id):
    category = Categories.objects.get(id=id)
    context = {"category": category}
    return render(request, "product/categori_info.html", context)


#def Buy(request):
    #return render(request, "product/index.html")


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'product/register_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'product/register.html', {'user_form': user_form})


class PricingListView(ListView):
    model = Pricing
    template_name = "product/index.html"


class PricingDetailView(DetailView):
    model = Pricing
    template_name = "product/prising.html"
