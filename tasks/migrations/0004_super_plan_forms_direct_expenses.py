# Generated by Django 3.1.1 on 2021-01-18 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20210116_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_plan_forms',
            name='direct_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='direct_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
    ]
