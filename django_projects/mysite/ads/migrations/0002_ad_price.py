# Generated by Django 4.0.7 on 2023-03-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
