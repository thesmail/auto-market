# Generated by Django 2.2.6 on 2019-10-14 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=50)),
                ('last_name', models.CharField(db_index=True, max_length=50)),
                ('phone', models.CharField(db_index=True, max_length=11)),
                ('note_c', models.CharField(blank=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=4)),
                ('vin', models.CharField(max_length=40)),
                ('body', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Client')),
            ],
        ),
    ]
