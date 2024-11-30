# Generated by Django 5.1.3 on 2024-11-28 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('crust_id', models.CharField(blank=True, editable=False, max_length=10, unique=True)),
                ('extra_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('extra_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sauce_id', models.CharField(blank=True, editable=False, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('multiplier', models.DecimalField(decimal_places=2, max_digits=4)),
                ('size_id', models.CharField(blank=True, editable=False, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vegetarian', models.BooleanField(default=False)),
                ('extra_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('topping_id', models.CharField(blank=True, editable=False, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('crust_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.crust')),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.sauce')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size')),
                ('toppings', models.ManyToManyField(related_name='pizzas', to='products.topping')),
            ],
        ),
    ]
