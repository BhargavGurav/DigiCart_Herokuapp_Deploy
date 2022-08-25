# Generated by Django 4.0.3 on 2022-08-23 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_image', models.ImageField(upload_to='cart')),
                ('category', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.FloatField()),
                ('item_disc', models.TextField()),
                ('quantity', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]
