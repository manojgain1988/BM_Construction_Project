# Generated by Django 4.2.7 on 2024-06-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0006_rename_instagram_ourteam_instagram_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
