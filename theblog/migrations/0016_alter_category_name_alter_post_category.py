# Generated by Django 4.2.1 on 2023-10-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0015_alter_post_category_alter_post_photo_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategorised', max_length=100),
        ),
    ]