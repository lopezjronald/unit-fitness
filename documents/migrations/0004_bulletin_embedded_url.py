# Generated by Django 4.0.5 on 2022-07-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_alter_document_embedded_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='embedded_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
