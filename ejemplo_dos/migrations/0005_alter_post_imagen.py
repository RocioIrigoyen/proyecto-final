# Generated by Django 4.1.3 on 2022-12-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo_dos', '0004_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null='True', upload_to='posts'),
        ),
    ]
