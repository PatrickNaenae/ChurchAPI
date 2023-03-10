# Generated by Django 4.1.6 on 2023-02-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('ME', 'Male'), ('FE', 'Female')], default='ME', max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership',
            field=models.CharField(choices=[('MR', 'Minister'), ('WR', 'Worker'), ('MB', 'Member'), ('FR', 'First timer')], default='MR', max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='occupation',
            field=models.CharField(choices=[('ST', 'Student'), ('BS', 'Business'), ('CE', 'Corporate'), ('UD', 'Unemployed'), ('OS', 'Others')], default='ST', max_length=200),
        ),
    ]
