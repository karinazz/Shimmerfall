from django.shortcuts import render

from . models import Cathegory, Product

from django.shortcuts import get_object_or_404

def store(request):

    all_products = Product.objects.all()

    context = {'my_products': all_products}

    return render(request, 'store/store.html', context)


def home(request):

    return render (request, 'store/home.html')


def tour(request):

    return render (request, 'store/tour.html')


def music(request):

    return render (request, 'store/music.html')



def categories(request):

    all_categories = Cathegory.objects.all()

    return {'all_categories': all_categories}

def list_category(request, category_slug=None):  

    category = get_object_or_404(Cathegory, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html', {'category':category, 'products':products})


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {'product' : product}

    return render (request, 'store/product-info.html', context)


