# Generated by Django 4.0.4 on 2022-06-13 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_event_event_status_delete_eventstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='amount',
            new_name='payment_amount',
        ),
    ]