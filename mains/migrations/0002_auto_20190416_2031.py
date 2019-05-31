# Generated by Django 2.1.7 on 2019-04-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='heroes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('rewards', models.TextField()),
                ('lived', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(),
        ),
    ]