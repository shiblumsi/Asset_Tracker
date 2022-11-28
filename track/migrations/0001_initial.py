# Generated by Django 4.0.4 on 2022-11-28 09:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('alias', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(choices=[('PHONE', 'Phone'), ('TABLET', 'Tablet'), ('LAPTOP', 'Laptop')], max_length=200)),
                ('model_no', models.CharField(max_length=200)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DelegateTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_out_at', models.DateTimeField(default=datetime.datetime.now)),
                ('condition', models.CharField(blank=True, max_length=200, null=True)),
                ('assets', models.ManyToManyField(blank=True, null=True, related_name='asset', to='track.asset')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GiveBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned_condition', models.CharField(max_length=200)),
                ('returned_date', models.DateTimeField(default=datetime.datetime.now)),
                ('delegat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_name', to='track.delegateto')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_model', to='track.asset')),
            ],
        ),
        migrations.AddField(
            model_name='delegateto',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delegateto', to='track.employee'),
        ),
    ]
