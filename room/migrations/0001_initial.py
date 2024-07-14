# Generated by Django 4.2.3 on 2024-07-14 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Duration', models.DurationField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='')),
                ('capacity', models.CharField(max_length=50)),
            ],
        ),
    ]
