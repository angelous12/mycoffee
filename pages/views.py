from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from orders.models import Order, OrderDetails
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    CATID = request.GET.get('category')
    if CATID :
        search = Product.objects.filter(category = CATID)
    else:
        search = Product.objects.all()
    name = None
    #search = Product.objects.all()
    categories = Category.objects.all()
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            search = search.filter(name__icontains=name)
    paginator = Paginator(search, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'productall':page_obj,
        'categories':categories,
    }
    return render(request , 'pages/index.html',context)


def product(request, slug):
    product_detail = Product.objects.get(slug=slug)
    context = {
        'pro':product_detail,
    }
    return render(request , 'product/product.html', context)