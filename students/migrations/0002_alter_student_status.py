# Generated by Django 5.0.14 on 2025-07-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(default='Activate', max_length=20),
        ),
    ]
