# Generated by Django 5.0.4 on 2024-04-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_emailaccept_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaccept',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]