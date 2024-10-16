# Generated by Django 5.1.2 on 2024-10-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='statements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psid', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50)),
            ],
            options={
                'verbose_name': 'Problem Statement',
                'verbose_name_plural': 'Problem Statements',
            },
        ),
    ]
