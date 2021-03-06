# Generated by Django 3.0.7 on 2020-07-21 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('thumbnail', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('guidelines', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='ChallengesParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_time', models.DateTimeField()),
                ('submission_time', models.DateTimeField()),
                ('feedback', models.TextField(blank=True)),
                ('challenge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='challenge.Challenge')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Domain'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
