# Generated by Django 4.2.4 on 2023-08-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_universities_field_of_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='universities',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
