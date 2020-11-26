# Generated by Django 3.1.1 on 2020-11-26 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('owner', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='industry/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Packs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='package/')),
                ('plan', models.CharField(max_length=3000)),
                ('validity', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_management.industries')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_management.packs')),
            ],
        ),
        migrations.CreateModel(
            name='User_bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_management.templates')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.user_db')),
            ],
        ),
    ]
