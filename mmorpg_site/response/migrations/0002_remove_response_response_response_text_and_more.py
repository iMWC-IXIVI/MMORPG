# Generated by Django 5.0.4 on 2024-04-10 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('response', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='response',
        ),
        migrations.AddField(
            model_name='response',
            name='text',
            field=models.CharField(default=1, max_length=100, verbose_name='Response'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='response',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time created'),
        ),
        migrations.AlterField(
            model_name='response',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
