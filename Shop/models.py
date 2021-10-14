from django.db import models
from User.models import PortalUser



class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(PortalUser, default=True, on_delete=models.CASCADE, related_name='shop_owner')
    shop_file = models.FileField(upload_to='media/images/shop/file/')
    established_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media/images/shop/image/')
    pan_no = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    opening_time = models.DateTimeField(auto_now_add=True)
    closing_time = models.DateTimeField(auto_now_add=True)
    # shop_category = models.ForeignKey(ShopCategory, on_delete = models.CASCADE)
    created_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.name







