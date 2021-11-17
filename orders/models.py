from django.db import models

from products.models import ProductModel


class OrderModel(models.Model):
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    city = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=60, null=True)

    products = models.ManyToManyField(ProductModel, related_name='orders')
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'