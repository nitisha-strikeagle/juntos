# Generated by Django 2.2.5 on 2020-01-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200128_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_image',
            field=models.ImageField(default='sdsds', upload_to='news/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
