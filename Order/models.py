# from django.db import models
# from User.models import PortalUser
# from Shop.models import Shop, ShopItem


# class Order(models.Model):
#     user = models.ForeignKey(PortalUser, on_delete=models.CASCADE)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     STATUS = (
#         ('Delivered', 'Delivered'),
#         ('On the way', 'On the way'),
#         ('Pending','Pending'),
#     )

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     shop_item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
#     ordered_date = models.DateTimeField(auto_now_add=True)
#     quantity = models.IntegerField()