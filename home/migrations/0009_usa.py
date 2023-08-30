# Generated by Django 4.2.4 on 2023-08-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_germany'),
    ]

    operations = [
        migrations.CreateModel(
            name='USA',
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
