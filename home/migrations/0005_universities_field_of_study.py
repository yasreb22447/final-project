# Generated by Django 4.2.4 on 2023-08-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_universities_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='universities',
            name='Field_of_study',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
