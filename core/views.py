from time import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

#def index(request):
#    return HttpResponse("Hello, world. You're at the core index.")


# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products':products})
