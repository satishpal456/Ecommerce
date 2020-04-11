from celery import Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//')
from ecommerce_app.models import Product


# USING TASK SCHEDULER WE CHECK AVAILIBITY OF PRODUCT"
@app.task
def check_product(productId):
    product = Product.objects.get(pk=productId)
    if product.stock == "IN STOCK":
        return True
    return False