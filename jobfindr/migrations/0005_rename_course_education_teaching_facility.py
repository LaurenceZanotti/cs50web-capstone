# Generated by Django 4.0.7 on 2022-09-29 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobfindr', '0004_alter_profile_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='course',
            new_name='teaching_facility',
        ),
    ]
