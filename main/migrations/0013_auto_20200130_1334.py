# Generated by Django 2.2.5 on 2020-01-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200130_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organization_city',
            field=models.CharField(default='Delhi', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='organization_contact_email',
            field=models.EmailField(default='abd@gef.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='organization_country',
            field=models.CharField(default='India', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]
