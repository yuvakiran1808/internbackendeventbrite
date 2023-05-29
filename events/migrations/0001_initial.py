# Generated by Django 4.2.1 on 2023-05-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('data', models.TextField()),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('is_liked', models.BooleanField(default=False)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
