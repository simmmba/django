# Generated by Django 2.1.5 on 2022-06-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ip',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
