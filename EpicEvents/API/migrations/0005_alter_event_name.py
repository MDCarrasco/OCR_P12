# Generated by Django 4.0.4 on 2022-06-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]