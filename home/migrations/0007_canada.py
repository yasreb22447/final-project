# Generated by Django 4.2.4 on 2023-08-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_universities_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='canada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Field_of_study', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('time', models.DateTimeField(null=True)),
                ('Degree', models.CharField(max_length=225, null=True)),
                ('funding_type', models.CharField(max_length=255, null=True)),
                ('Eligible_Countreies', models.CharField(max_length=255, null=True)),
                ('link', models.URLField(null=True)),
            ],
        ),
    ]
