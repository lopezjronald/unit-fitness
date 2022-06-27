# Generated by Django 4.0.5 on 2022-06-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Appointment Letter', 'Appointment Letter'), ('Google Form', 'Google Form'), ('Information', 'Information'), ('PT Form', 'PT Form')], max_length=50, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('embedded_url', models.URLField(blank=True, null=True)),
                ('document_created', models.DateTimeField(auto_now_add=True)),
                ('document_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
