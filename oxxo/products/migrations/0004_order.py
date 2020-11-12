# Generated by Django 3.1.3 on 2020-11-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201111_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.beer')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
            ],
        ),
    ]