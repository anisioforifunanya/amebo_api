# Generated by Django 5.0.1 on 2024-03-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_likes_alter_events_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='tags',
        ),
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_type',
            field=models.CharField(choices=[('physical', 'Physical'), ('virtual', 'Virtual'), ('hybrid', 'Hybrid')], default='physical', max_length=255, verbose_name='Event Type'),
        ),
    ]