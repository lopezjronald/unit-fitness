# Generated by Django 4.0.5 on 2022-06-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assessment',
            options={'ordering': ['date', 'time']},
        ),
    ]
