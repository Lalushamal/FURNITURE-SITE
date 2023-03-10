# Generated by Django 4.1 on 2022-12-21 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_measurment', models.TextField()),
                ('product_small', models.TextField()),
                ('product_large', models.TextField()),
                ('product_warrenty', models.TextField()),
                ('product_brand', models.CharField(max_length=100)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.furniture')),
            ],
        ),
    ]
