import operator
import functools
import logging
import csv

from time import timezone
from core.forms import ProductForm, UploadFileForm
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q

from .models import Product

log = logging.getLogger(__name__)

#def index(request):
#    return HttpResponse("Hello, world. You're at the core index.")

# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


class ProductListView(ListView):
    paginate_by = 48
    #products = Product.objects.all()
    template_name = "product/list.html"
    def get_queryset(self):
        return Product.objects.all()

    #return render(request, 'product/list.html', {'products':products})


class ProductSearchListView(ProductListView):
    """
    Display a product list page filtered by the search query.
    """
    paginate_by = 48
    model = Product
    template_name = "product/list.html"

    def get_queryset(self):
        result = super(ProductListView, self).get_queryset()
        query = self.request.GET.get('q')

        if query:
            query_list = query.split()

            log.error("query list: %s " % query_list)

            # 1. Complex search filters
            # result = result.filter(
            #     reduce(operator.and_,
            #            (Q(name__icontains=q) for q in query_list))|
            #     reduce(operator.and_,
            #            (Q(manufacturer__name__icontains=q) for q in query_list))|
            #     reduce(operator.and_,
            #            (Q(category__name__icontains=q) for q in query_list))|
            #     reduce(operator.and_,
            #            (Q(description__icontains=q) for q in query_list))
            # )

            # 2. Simple fulltext search of description field
            #result = Product.objects.filter(description__search=query)

            # 3. Advanced fulltext search over multiple fields
            #result = Product.objects.annotate(search = SearchVector('name', 'description', 'manufacturer__name',)).filter(search=query)

            # 4. Advanced fulltext search with weights, order results by rank in descending order
            vector = SearchVector('name', weight='A') + SearchVector('category__name', weight='A') + SearchVector('manufacturer__name', weight='B') + SearchVector('description', weight='C')
            query = SearchQuery(query)
            rank = SearchRank(vector, query)
            result = Product.objects.annotate(rank=rank).filter(rank__gte=0.01).order_by('-rank')

            # q = 'hello world'
            # queryset = Product.objects.extra(
            #     select={
            #         'snippet': "ts_headline(body, query)",
            #         'rank': "ts_rank_cd(body_tsv, query, 32)",
            #     },
            #     tables=["plainto_tsquery(%s) as query"],
            #     where=["body_tsv @@ query"],
            #     params=[q]
            # ).order_by('-rank')
            #
            # for entry in queryset:
            #     print entry.title, entry.snippet, entry.rank

            # 5. Assign custom weights to D, C, B, A ranking
            #rank = SearchRank(vector, query, weights=[0.2, 0.4, 0.6, 0.8])
            #Product.objects.annotate(rank=rank).filter(rank__gte=0.3).order_by('-rank')

        return result


def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render (request, 'product/show.html', {'product':product})


class ProductCreateView(CreateView):
    model = Product
    template_name = "product/create.html"
    success_url = "/products"
    fields = ['code', 'name', 'description', 'created_by', 'manufacturer']


class ProductUpdateView(UpdateView):
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
        return super(ProductUpdateView, self).save(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ProductUpdateView, self).form_valid(form)


class ProductDeleteView(DeleteView):
    template_name = 'product/delete.html'
    model = Product
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('product-list-view')


# def upload(request):
#     log.info("upload file %s", request)
#
#     if request.method == 'POST' and request.FILES['myfile']:
#         file = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(file.name, file)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'product/upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'product/upload.html')



def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            log.info("form %s", form)

            form.save()
            #file = form.cleaned_data['myfile']

            #handle_uploaded_file(file)

            #return HttpResponseRedirect('/products/')
    else:
        form = UploadFileForm()

    return render(request, 'product/upload.html', {'form': form})


def handle_uploaded_file(file):
    pass
    # reader = csv.reader(file)
    # for row in reader:
    #     print row
    #

