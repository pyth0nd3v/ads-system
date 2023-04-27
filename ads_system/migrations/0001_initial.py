# Generated by Django 3.2.12 on 2023-04-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=3)),
                ('max_daily_visitors', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('visitors_need', models.PositiveIntegerField()),
                ('cities', models.ManyToManyField(related_name='ads', to='ads_system.Location')),
            ],
        ),
    ]