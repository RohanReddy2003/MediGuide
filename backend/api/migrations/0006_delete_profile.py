# Generated by Django 4.2.4 on 2023-10-01 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_profile_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
