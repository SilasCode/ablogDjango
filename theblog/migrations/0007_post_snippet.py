# Generated by Django 4.1.6 on 2023-09-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link to read blog', max_length=255),
        ),
    ]
