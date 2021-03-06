# Generated by Django 2.1.5 on 2022-06-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도,위도 포맷으로 입력', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 입력해주세요. 최대 100자 내외', max_length=100, verbose_name='제목'),
        ),
    ]
