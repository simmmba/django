# Generated by Django 2.1.5 on 2022-06-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]