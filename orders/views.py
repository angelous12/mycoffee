from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from pages.models import Product
from .models import Order,OrderDetails, Coupon
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def add_to_cart(request):
    if 'pro_id' in request.GET and 'qty' in request.GET and 'price' in request.GET and request.user.is_authenticated and not request.user.is_anonymous:
        pro_id = request.GET['pro_id']
        qty    = request.GET['qty']
        order = Order.objects.filter(user = request.user , is_finished=False)
        pro = Product.objects.get(slug=pro_id)
        if order:
            old_order = Order.objects.get(user = request.user , is_finished=False)
            orderdetails = OrderDetails.objects.create(product=pro , order = old_order , price = pro.price , quantity=qty)
            messages.success(request , 'Was Added To Cart For Old Order')
        else:
            new_order = Order()
            new_order.user = request.user
            new_order.order_date = timezone.now()
            new_order.is_finished = False
            new_order.save()
            orderdetails = OrderDetails.objects.create(product=pro , order = new_order , price = pro.price , quantity=qty)
            messages.success(request , 'Was Added To Cart For New Order')
        return redirect ('/product/'+request.GET['pro_id'])

    else:
        messages.error(request , 'You must be logged in')
        return redirect ('/product/'+request.GET['pro_id'])

def cart(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        if 'name-coupon' in request.GET:
            namerequset = request.GET['name-coupon']
            models = Coupon.objects.filter( coupon = namerequset)
            if models:
                messages.success(request, 'Success coupon')
                return redirect('cart')
            else:
                messages.error(request , 'coupon error')
                return redirect('cart')

        else:
            models = Product.objects.all()

        if Order.objects.filter(user = request.user , is_finished= False):
            order = Order.objects.get(user = request.user , is_finished=False)
            orderdetails = OrderDetails.objects.filter(order = order)
            total = 0
            for sub in orderdetails:
                total += sub.price * sub.quantity
            couponss = Coupon.objects.filter(is_active = True)
            context = {
                'order':order,
                'orderdetails':orderdetails,
                'total':total,
                'models':models,
                'couponss':couponss,
            }
    else:
        pass
    return render(request , 'orders/cart.html', context)

def remove_cart(request ,id): 
   if request.user.is_authenticated and not request.user.is_anonymous and id:
       orderdetails = OrderDetails.objects.get(id = id)
       if orderdetails.order.user.id == request.user.id:
            orderdetails.delete() 
   return redirect ('cart')

