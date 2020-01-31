# Generated by Django 2.2.5 on 2020-01-30 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_auto_20200130_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambassador',
            name='organization',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='ambassador', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='organization',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='careers', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spreadword',
            name='organization',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='spreadword', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]