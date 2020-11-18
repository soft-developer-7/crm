# Generated by Django 3.1.1 on 2020-11-17 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_db',
            name='countrycode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='user_current_super_plan_forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=5, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.super_plan_forms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.user_db')),
            ],
        ),
    ]
