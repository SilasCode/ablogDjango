# Generated by Django 4.1.6 on 2023-09-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_post_video_file_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo_credit',
            field=models.CharField(blank=True, default='coding', max_length=255, null=True),
        ),
    ]
