# Generated by Django 2.2 on 2020-07-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20200704_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
