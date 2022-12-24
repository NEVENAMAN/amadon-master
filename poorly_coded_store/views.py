from django.shortcuts import render,redirect
from .models import *

def index(request):
    if 'total_quantity' in request.session:  
        request.session['total_quantity'] = 0
        request.session['total_price'] = 0
    else:
        request.session['total_quantity'] = 0
        request.session['total_price'] = 0
        
    print("quantity 1 : " , request.session['total_quantity'] )
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)
    

def checkout(request):
    if request.method == "POST" :
        id = request.POST['product_id']
        product = Product.objects.get(id=id)
        request.session['price'] = float(product.price)
        print("***price :" ,request.session['price'])
        quantity = int(request.POST['quantity'])
        print("***quantity :" , request.session['quantity'])
        total_charge = request.session['quantity']* request.session['price']
        print("***total price :" , request.session['total_charge'])
        AddOrder(quantity,total_charge,product)
        request.session['total_quantity'] += quantity
        print("quantity 2 : " , request.session['total_quantity'] )
        request.session['total_price'] += total_charge
        print("amount : " , request.session['total_price'])
    return redirect('/test')

def test(request):
    print("quantity 1 : " , request.session['total_quantity'] )
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def Report_buy(request):
    print("quantity 3: " , request.session['total_quantity'] )

    context = {
        "price_of_last_item" : request.session['price'] ,
        "quantity" : request.session['total_quantity'],
        "amount" : request.session['total_price']
    }
    return render(request, "store/checkout.html" , context)





