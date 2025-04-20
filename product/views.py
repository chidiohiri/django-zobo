from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .models import Product, Checkout
from . import form as fm 
from .filters import CheckoutFilter

User = get_user_model()

@login_required
def add_product(request):
    if request.method == 'POST':
        form = fm.AddProductForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user 
            var.save()

            user = User.objects.get(pk=request.user.pk)
            user.has_product = True
            user.save()

            messages.success(request, 'Product has been added and saved to Database')
            return redirect('product-details')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('add-product')
    else:
        form = fm.AddProductForm()
        context = {'form':form}
    return render(request, 'product/add_product.html', context)

@login_required
def update_product(request):
    product = Product.objects.first()

    if request.method == 'POST':
        form = fm.UpdateProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Product information is now updated and saved to Database')
            return redirect('dasboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-product', product.pk)
    else:
        form = fm.UpdateProductForm(instance=product)
        context = {'product':product, 'form':form}
    return render(request, 'product/update_product.html', context)

def product_details(request): # this would be the home page
    product = Product.objects.first()
    context = {'product':product}
    return render(request, 'product/product_details.html', context)

def check_out(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.CheckoutForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.product = product
            var.total_amount = int(var.amount) * int(product.price) + 2000
            var.save()

            # Save var.id (or any unique identifier) in session
            request.session['checkout_id'] = var.id

            return redirect('initialize-payment')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('checkout', product.pk)
    else:
        form = fm.CheckoutForm()
        context = {'form':form, 'product':product}
    return render(request, 'product/checkout.html', context)

@login_required
def order_history(request):
    history = Checkout.objects.filter(is_verified=True).order_by('-timestamp')

    # apply filter 
    history_filter = CheckoutFilter(request.GET, queryset=history)
    filtered_invoices = history_filter.qs

    # pagination
    paginator = Paginator(filtered_invoices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'history':page_obj, 'filter':history_filter}
    return render(request, 'product/order_history.html', context)

