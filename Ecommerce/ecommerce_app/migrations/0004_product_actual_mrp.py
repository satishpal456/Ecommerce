# Generated by Django 3.0 on 2020-04-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='actual_mrp',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
