# Generated by Django 4.0.6 on 2022-08-31 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_img', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('social_github', models.CharField(blank=True, max_length=200, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('social_website', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
