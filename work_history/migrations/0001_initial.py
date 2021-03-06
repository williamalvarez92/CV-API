# Generated by Django 3.2.9 on 2021-12-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('role_tile', models.CharField(max_length=100, null=True)),
                ('place', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('company_url', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
