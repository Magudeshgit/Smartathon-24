# Generated by Django 5.1.2 on 2024-10-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_hackathonreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathonreg',
            name='ch',
            field=models.CharField(default='2323', max_length=87),
            preserve_default=False,
        ),
    ]
