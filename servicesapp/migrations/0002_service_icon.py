# Generated by Django 4.2.7 on 2024-06-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default='d', max_length=200),
            preserve_default=False,
        ),
    ]
