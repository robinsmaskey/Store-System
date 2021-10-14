from django.contrib import admin

# Register your models here.
from Item.models import Item, ItemCategory

admin.site.register(Item)
admin.site.register(ItemCategory)




