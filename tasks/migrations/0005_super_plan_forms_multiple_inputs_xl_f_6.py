# Generated by Django 3.1.1 on 2021-03-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210228_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_plan_forms_multiple_inputs_xl',
            name='f_6',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
