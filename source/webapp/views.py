from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product



def index_view(request):

    products = Product.objects.all()
    return render(request, 'index.html', context={
        'products': products

    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={

        'product': product

    })



def product_create_view(request, *args, **kwargs):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method =='POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price']

            )
            return redirect('product_detail_view', pk=product.pk)
        else:
            return render(request, 'create.html', context={'form': form,})