# Generated by Django 3.0 on 2020-04-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quatity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
