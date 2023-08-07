# Generated by Django 4.2.3 on 2023-07-21 16:30

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_profile_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='post_imgs')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('num_of_likes', models.IntegerField(default=0)),
            ],
        ),
    ]
