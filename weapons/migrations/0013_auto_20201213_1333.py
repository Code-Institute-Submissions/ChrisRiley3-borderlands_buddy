# Generated by Django 3.0.8 on 2020-12-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0012_auto_20201213_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='image_url',
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='manufacture',
            field=models.CharField(max_length=254),
        ),
    ]
