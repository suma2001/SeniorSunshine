# Generated by Django 3.1.3 on 2020-12-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elder',
            name='request_service',
            field=models.SmallIntegerField(default=0),
        ),
    ]