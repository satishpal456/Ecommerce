from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Q
from django.core.mail import EmailMessage
from .models import *
from django.contrib.auth.decorators import login_required
from Ecommerce.tasks import check_product
from django.core.mail import send_mail

from Ecommerce import settings


class Login(View):
    '''User can logged in here using username and password'''

    def get(self,*args,**kwargs):
        return render(self.request,"login.html")

    def post(self,*args,**kwargs):
        try:
            data = self.request.POST.get
            user = authenticate(username=data("username"), password=data("password"))
            if user is not None:
                login(self.request, user)
                return redirect("home")
            else:
                return HttpResponse("unauthorized access")
        except Exception as e:
            return HttpResponse("something wrong {0}".format(e))


class Home(View):

    '''It is home page where user can see all product list'''

    @method_decorator(login_required)
    def get(self,*args,**kwargs):
        try:
            product = Product.objects.all()
            return render(self.request,"home.html",{"product":product})
        except Exception as e:
            return HttpResponse("something wrong {0}".format(e))

@method_decorator(csrf_exempt, name='dispatch')
class Cart(View):
    '''HERE USER CAN ADD PRODUCT IT'S OWN CART'''
    @method_decorator(login_required)
    def get(self,*args,**kwargs):
        try:
            cart_data = CartProducts.objects.filter(user=self.request.user)
            sum_value = cart_data.aggregate(Sum('product__price'))
            GST =  (sum_value["product__price__sum"] * 18) / 100
            after_gst_price = sum_value["product__price__sum"] - GST
            return render(self.request,"cart.html",{"cart_data":cart_data,"after_gst_price":after_gst_price,"GST":GST})
        except Exception as e:
            return HttpResponse("something wrong {0}".format(e))

    @method_decorator(login_required)
    def post(self,*args,**kwargs):
        try:
            data = self.request.POST.get
            cart = CartProducts.objects.create(user_id=data("user"),product_id=data("product"))
            return JsonResponse(data={"data":1})
        except Exception as e:
            return HttpResponse("something wrong {0}".format(e))

class Search(View):
    '''user can serch product they can search product using product-name and  price of product'''
    @method_decorator(login_required)
    def post(self,*args,**kwargs):
        try:
            data = self.request.POST.get
            product = Product.objects.filter(Q(name__icontains=data("search_input")) | Q(price__icontains=data("search_input")))
            return render(self.request,"home.html",{"product":product})
        except Exception as e:
            return HttpResponse("something wrong {0}".format(e))


@login_required(login_url='/login/')
def logoutView(request):
    logout(request)
    return redirect("login")

def product_email(subject,message,recipient_list):
    '''email sent function'''
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, [recipient_list] )

class Checkout(View):
    '''USER CAN CHECKOUT IT'S PRODUCT'''
    @method_decorator(login_required)
    def post(self,*args,**Kwargs):
        try:
            cart_data = CartProducts.objects.filter(user=self.request.user)
            for data in cart_data:
                status = check_product(data.product.id)
            user_email = self.request.user.email
            if status == True:
                print("Product Buy Your Item has been successfully Purchased")
                email = product_email('Product Buy', 'Your Item has been successfully Purchased', user_email)
                return HttpResponse("Product Sucessfully Purchased PLease check Your email")
            else:
                print("Product Fail to Buy Your becuase of OUT OF STOCK.")
                email = product_email('Product Fail', 'Product out of stock', user_email)
            email.send()
            return HttpResponse("Product out of stock")
        except Exception as e:
            return HttpResponse("something wrong {0}".format(e))


