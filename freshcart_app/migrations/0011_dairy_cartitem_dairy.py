# Generated by Django 5.1 on 2024-10-07 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshcart_app', '0010_wishlistitem_quantity_alter_wishlistitem_fruit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dairy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='image/dairy/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='dairy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freshcart_app.dairy'),
        ),
    ]
