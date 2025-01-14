# Generated by Django 5.0.1 on 2024-02-28 23:20

import django.core.serializers.json
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_appusers_profile_pic_url_appusers_verify_pic_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('organizer', models.CharField(blank=True, max_length=500, null=True)),
                ('event_type', models.CharField(choices=[('appearance_singing', 'Appearance or Singing'), ('attraction', 'Attraction'), ('camp_trip_retreat', 'Camp, Trip, or Retreat'), ('class_train_workshop', 'Class, Training, or Workshop'), ('concert_performance', 'Concert or Performance'), ('conference', 'Conference'), ('convention', 'Convention'), ('dinner_gala', 'Dinner or Gala'), ('festival_fair', 'Festival or Fair'), ('game_competiotion', 'Game or Competion'), ('meeting_network_event', 'Meeting or Network Event'), ('other', 'Other'), ('party_social_gathering', 'Party or Social Gathering'), ('race_endurance_event', 'Race or Endurance Event'), ('rally', 'Rally'), ('screening', 'Screening'), ('seminar_talk', 'Seminar or Talk'), ('tour', 'Tour'), ('tournament', 'Tournament'), ('trade_consumer_show', 'Trade Show, Consumer Show or Expo')], default='tour', max_length=255, verbose_name='Event Type')),
                ('category', models.CharField(choices=[('auto_boat_air', 'Auto, Boat & Air'), ('business_professional', 'Business & Professional'), ('charity_causes', 'Charity & Causes'), ('community_culture', 'Community & Culture'), ('family_education', 'Family & Education'), ('fashion_beauty', 'Fashion & Beauty'), ('film_media_ent', 'Film, Media & Entertainment'), ('food_drink', 'Food & Drink'), ('government_politics', 'Government & politics'), ('health_wellness', 'Health & Wellness'), ('Hobbies_special_nterest', 'Hobbies & Special Interest'), ('home_lifestyle', 'Home & Lifestyle'), ('music', 'Music'), ('other', 'Other'), ('performing_visual_arts', 'Performing & Visual Arts'), ('religion_spirituality', 'Religion & Spirituality'), ('school_activities', 'School Activities'), ('science_technology', 'Science & Technology'), ('seasonal_holiday', 'Seasonal & Holiday'), ('sports_fitness', 'Sports & Fitness'), ('travel_outdoor', 'Travel & Outdoor')], default='music', max_length=255, verbose_name='Event Category')),
                ('tags', models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
                ('location', models.CharField(blank=True, max_length=1500, null=True)),
                ('virtual_url', models.URLField(blank=True, max_length=500, null=True)),
                ('date', models.CharField(blank=True, max_length=500, null=True)),
                ('time', models.CharField(blank=True, max_length=500, null=True)),
                ('picture', models.URLField(blank=True, max_length=1500, null=True)),
                ('google_map_link', models.URLField(blank=True, max_length=1500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.appusers')),
            ],
        ),
    ]
