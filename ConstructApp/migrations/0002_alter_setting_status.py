# Generated by Django 4.2.7 on 2024-06-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConstructApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50),
        ),
    ]
