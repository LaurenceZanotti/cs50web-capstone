# Generated by Django 4.0.7 on 2022-09-29 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobfindr', '0005_rename_course_education_teaching_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='experience',
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='jobfindr.profile'),
        ),
        migrations.AddField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='jobfindr.profile'),
        ),
    ]
