# Generated by Django 5.1.2 on 2024-10-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_statements_psid_statements_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='statements',
            name='submissions',
            field=models.IntegerField(default=20),
        ),
    ]
