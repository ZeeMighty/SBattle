# Generated by Django 2.1.7 on 2019-05-07 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0004_auto_20190421_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='heroes',
        ),
        migrations.AddField(
            model_name='heroe',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mains.event'),
        ),
    ]
