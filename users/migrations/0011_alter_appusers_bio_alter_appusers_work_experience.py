# Generated by Django 5.0.1 on 2024-04-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_appusers_other_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusers',
            name='bio',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='appusers',
            name='work_experience',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
