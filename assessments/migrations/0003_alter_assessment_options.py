# Generated by Django 4.0.5 on 2022-06-28 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_alter_assessment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assessment',
            options={'ordering': ['-date', 'time']},
        ),
    ]
