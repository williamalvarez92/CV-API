# Generated by Django 3.2.9 on 2021-12-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100, null=True)),
                ('education_type', models.CharField(max_length=100, null=True)),
                ('field_of_study', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
