import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, SubCategory, SpecialOffer
from .forms import ProductForm


def tools_dropdown(request):
    with open('products/fixtures/sub_category.json', 'r') as file:
        sub_category_data = json.load(file)

    context = {
        'sub_categories': sub_category_data,
    }

    return render(request, 'tools_dropdown_template.html', context)


def all_products(request, category=None, sub_category=None, special_offer=None):  # noqa
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    friendly_current_category = None
    friendly_current_sub_category = None
    friendly_current_special_offer = None

    special_offer_name = request.GET.get('special_offer')
    selected_category = request.GET.get('category')
    selected_sub_category = request.GET.get('sub_category')
    search_query = request.GET.get('q')

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        elif sortkey == 'category':
            sortkey = 'category__name'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if selected_category and selected_sub_category:
        products = products.filter(category__name=selected_category, sub_category__name=selected_sub_category)  # noqa

    if selected_category:
        current_category = Category.objects.filter(name=selected_category).first()  # noqa
        if current_category:
            friendly_current_category = current_category.get_friendly_name()

    if selected_category:
        current_category = Category.objects.filter(name=selected_category).first()  # noqa
        if current_category:
            friendly_current_category = current_category.get_friendly_name()

    if sub_category:
        current_sub_category = SubCategory.objects.filter(name=sub_category).first()  # noqa
        if current_sub_category:
            friendly_current_sub_category = current_sub_category.get_friendly_name()  # noqa

    if special_offer_name:
        products = products.filter(special_offer__name=special_offer_name)
        # friendly name for the special offer
        current_special_offer = SpecialOffer.objects.filter(name=special_offer_name).first()  # noqa
        if current_special_offer:
            friendly_current_special_offer = current_special_offer.get_friendly_name()  # noqa

    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))  # noqa

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'product': products,
        'search_term': search_query,
        'current_sorting': current_sorting,
        'current_categories': categories,
        'current_category': friendly_current_category,
        'current_sub_category': friendly_current_sub_category,
        'current_special_offer': friendly_current_special_offer,
        'special_offers': SpecialOffer.objects.values_list('name', flat=True).distinct()  # noqa
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, ('Failed to add product. Please ensure the form is valid.'))  # noqa
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, ('Failed to update product. Please ensure the form is valid.'))  # noqa
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('all_products'))


def home(request):
    return render(request, 'base.html')
