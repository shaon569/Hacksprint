# Generated by Django 3.0.7 on 2020-07-23 12:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_auto_20200723_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='slug',
            field=models.SlugField(default=uuid.UUID('e5904551-42a5-4de5-96fa-415339a275d4'), max_length=250),
        ),
        migrations.AlterField(
            model_name='track',
            name='slug',
            field=models.SlugField(default=uuid.UUID('54a8bfc3-e350-420b-89e9-d88b6cc22df4'), max_length=250),
        ),
    ]
