# Generated by Django 5.1.4 on 2025-01-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bk_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bk_name',
            field=models.CharField(max_length=100),
        ),
    ]
