# Generated by Django 2.2.5 on 2020-01-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200102_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
