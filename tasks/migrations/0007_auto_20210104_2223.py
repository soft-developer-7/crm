# Generated by Django 3.1.1 on 2021-01-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20210104_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_plan_forms',
            name='capex_additions_intangible_or',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='super_plan_forms',
            name='capex_additions_or',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='super_plan_forms',
            name='capex_deletions_or',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
