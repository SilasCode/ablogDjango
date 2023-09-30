# Generated by Django 4.1.6 on 2023-09-22 19:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0012_post_post_highlighted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
