# Generated by Django 5.0.3 on 2024-04-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_app', '0011_remove_students_current_semister_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='batch',
            field=models.CharField(default=2078, max_length=4),
        ),
    ]
