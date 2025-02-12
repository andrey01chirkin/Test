# Generated by Django 5.1.4 on 2024-12-31 15:22

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='practice_app.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='concert',
            name='artists',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='concertmanager',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Concert',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
        migrations.DeleteModel(
            name='ConcertManager',
        ),
    ]
