# Generated by Django 3.1.3 on 2020-11-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lastName',
            field=models.TextField(default='Guest'),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.TextField(default='Guest'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.TextField(default='Guest'),
        ),
    ]
