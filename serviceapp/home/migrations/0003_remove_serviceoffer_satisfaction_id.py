# Generated by Django 2.2.5 on 2021-01-24 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210123_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceoffer',
            name='satisfaction_id',
        ),
    ]