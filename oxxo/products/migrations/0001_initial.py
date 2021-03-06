# Generated by Django 3.1.3 on 2020-11-11 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('alcohol', models.DecimalField(decimal_places=2, max_digits=4)),
                ('milliliters', models.IntegerField()),
                ('handcrafted', models.BooleanField()),
                ('nacinalty', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
