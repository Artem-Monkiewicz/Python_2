# Generated by Django 5.0.1 on 2024-05-24 03:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_viewer', '0009_alter_country_id_alter_country_region'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(choices=[('NEAR EAST', 'NEAR EAST'), ('BALTICS', 'BALTICS'), ('C.W. OF IND. STATES', 'C.W. OF IND. STATES'), ('NORTHERN AFRICA', 'NORTHERN AFRICA'), ('NORTHERN AMERICA', 'NORTHERN AMERICA'), ('EASTERN EUROPE', 'EASTERN EUROPE'), ('OCEANIA', 'OCEANIA'), ('SUB-SAHARAN AFRICA', 'SUB-SAHARAN AFRICA'), ('LATIN AMER. & CARIB', 'LATIN AMER. & CARIB'), ('WESTERN EUROPE', 'WESTERN EUROPE'), ('ASIA (EX. NEAR EAST)', 'ASIA (EX. NEAR EAST)')], max_length=500),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clcks_left', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
