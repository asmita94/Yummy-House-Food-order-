# Generated by Django 5.0.2 on 2024-02-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcommapp', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=1000),
        ),
    ]
