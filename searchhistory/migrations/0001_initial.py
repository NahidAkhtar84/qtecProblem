# Generated by Django 3.1.7 on 2021-03-28 15:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchkey', models.CharField(max_length=255)),
                ('searchtime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('historytitle', models.CharField(default='No searched title found!', max_length=1000)),
                ('historylink', models.CharField(default='www.notfound.com', max_length=1000)),
                ('historysummary', models.TextField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]