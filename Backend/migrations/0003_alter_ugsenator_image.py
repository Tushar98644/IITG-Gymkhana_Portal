# Generated by Django 4.1 on 2023-01-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_upcomingevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ugsenator',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]
