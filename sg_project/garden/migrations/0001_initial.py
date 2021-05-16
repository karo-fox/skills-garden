# Generated by Django 3.2.2 on 2021-05-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_reviewed', models.DateField()),
                ('review_frequency', models.DurationField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.field')),
            ],
        ),
    ]
