# Generated by Django 3.1.7 on 2021-05-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unverifieduser',
            name='code',
            field=models.CharField(default='000000', max_length=6),
        ),
    ]
