from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    products = models.ForeignKey(Product, related_name="orders", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def AddOrder(quantity,total_charge,product):
    return Order.objects.create(quantity_ordered=quantity, total_price=total_charge, products = product)

def Get_product_info(id):
    return Product.object.get(id = id)

def Get_order_info(id):
    return Order.objects.filter(products=id)

def Get_order_products_info(request):
    return Order.products.all()