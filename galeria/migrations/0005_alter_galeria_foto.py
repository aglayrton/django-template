# Generated by Django 5.1.3 on 2024-12-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_galeria_fotografia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]
