# Generated by Django 3.2.4 on 2021-06-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Console', '0007_alter_filedownloadobjectstat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedownloadobjectstat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
