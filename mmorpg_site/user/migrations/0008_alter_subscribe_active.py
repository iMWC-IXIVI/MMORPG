# Generated by Django 5.0.4 on 2024-04-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]