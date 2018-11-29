# Generated by Django 2.1.3 on 2018-11-29 01:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
