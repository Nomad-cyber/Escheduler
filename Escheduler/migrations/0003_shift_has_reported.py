# Generated by Django 4.2.6 on 2024-10-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escheduler', '0002_project_schedule_project_shift_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='has_reported',
            field=models.BooleanField(default=False),
        ),
    ]
