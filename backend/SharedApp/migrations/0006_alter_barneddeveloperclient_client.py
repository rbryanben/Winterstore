# Generated by Django 3.2.4 on 2021-07-05 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SharedApp', '0005_alter_developerclient_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barneddeveloperclient',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SharedApp.developerclient'),
        ),
    ]
