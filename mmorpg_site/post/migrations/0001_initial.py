# Generated by Django 5.0.4 on 2024-04-06 19:19

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_change', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Tanks', 'Tank'), ('Healers', 'Healer'), ('DD', 'DD'), ('Traders', 'Trader'), ('GuildMasters', 'Guild master'), ('ShareQuests', 'Share quest'), ('Blacksmiths', 'Blacksmith'), ('Tanners', 'Tanner'), ('PotionsBrewers', 'Potions brewers'), ('SpellMasters', 'Spell master')], max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
