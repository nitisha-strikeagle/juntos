# Generated by Django 2.2.5 on 2020-01-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200128_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]
