# Generated by Django 2.2 on 2020-06-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20200630_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
