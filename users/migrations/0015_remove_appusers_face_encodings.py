# Generated by Django 5.0.1 on 2024-05-15 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_appusers_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appusers',
            name='face_encodings',
        ),
    ]
