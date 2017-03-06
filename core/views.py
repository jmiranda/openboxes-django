from time import timezone

from core.forms import ProductForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, DeleteView, CreateView, UpdateView

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


def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render (request, 'product/show.html', {'product':product})


class product_create(CreateView):
    model = Product
    template_name = "product/create.html"
    success_url = "/products"
    fields = ['code', 'name', 'description', 'created_by', 'manufacturer']

class product_edit(UpdateView):
    template_name = 'product/edit.html'
    form_class = ProductForm
    model = Product
    #fields = ['code', 'name', 'description']
    pk_url_kwarg = 'product_id'
    #queryset = Product.objects.all()
    success_url = '/products/'

    def save(self, *args, **kwargs):
        print self.instance
        # returns <Profile: Billy Bob's Profile> instead of <User: Billy Bob> !!!
        return super(product_edit, self).save(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(product_edit, self).form_valid(form)

class product_delete(DeleteView):
    template_name = 'product/delete.html'
    model = Product
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('product_list')

