from django.db import models
from User.models import PortalUser
from Shop.models import Shop

class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    item_category = models.ForeignKey(ItemCategory, on_delete= models.CASCADE, default=True)
    image = models.ImageField(upload_to='media/images/Item/')
    is_published = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    expiry_date = models.DateTimeField(default=True)
    is_stocked = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE, default=True)
