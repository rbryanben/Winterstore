# Generated by Django 3.2.4 on 2021-06-29 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Console', '0003_filedownloadinstance_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedownloadinstance',
            name='stat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Console.filedownloadobjectstat'),
        ),
    ]
