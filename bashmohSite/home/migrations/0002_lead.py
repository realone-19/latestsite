# Generated by Django 3.2.3 on 2021-08-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('estate_name', models.IntegerField()),
                ('number_of_plots', models.CharField(max_length=30)),
                ('home_address', models.CharField(max_length=30)),
                ('office_address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
