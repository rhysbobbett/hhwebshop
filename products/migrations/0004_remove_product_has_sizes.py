# Generated by Django 4.2.6 on 2023-10-19 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_has_sizes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="has_sizes",
        ),
    ]
