# Generated by Django 3.1.7 on 2021-09-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0002_auto_20210914_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='itemcategory',
            name='created_by',
        ),
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='Item.itemcategory'),
        ),
    ]
