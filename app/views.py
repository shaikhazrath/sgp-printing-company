
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    # Get the product with the given product_id or return a 404 page if not found
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})