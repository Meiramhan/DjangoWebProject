from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200)
    open = models.BooleanField(default=False)

class Order(models.Model):
    STATUSES = (
        ('P', 'Готовится'),
        ('D', 'Доставка'),
        ('F', 'Завершён')
    )
    status = models.CharField(max_length=1, choices=STATUSES)
    amount = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)