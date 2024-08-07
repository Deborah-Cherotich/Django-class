# Generated by Django 5.0.6 on 2024-08-08 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_courses_delete_course'),
        ('room', '0002_rename_year_room_meeting_days_remove_room_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_the_week', models.DateField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='room.room')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='courses.courses')),
            ],
        ),
    ]
