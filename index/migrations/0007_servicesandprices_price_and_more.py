# Generated by Django 4.2 on 2023-04-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_phonenumber_servicesandprices_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesandprices',
            name='price',
            field=models.IntegerField(max_length=10, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='Телефонный номер'),
        ),
    ]
