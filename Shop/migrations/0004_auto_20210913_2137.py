# Generated by Django 3.1.7 on 2021-09-13 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_remove_shopcategory_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='shop_category',
        ),
        migrations.DeleteModel(
            name='ShopCategory',
        ),
    ]
