from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the core index.")


def product_list(request):
    return render(request, 'product/list.html', {})