# Generated by Django 3.1.1 on 2021-02-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20210203_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super_plan_forms',
            old_name='projection_tabl',
            new_name='projection_table',
        ),
    ]