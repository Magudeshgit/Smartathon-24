# Generated by Django 5.1.2 on 2024-10-20 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_delete_hackathonreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='hackathonreg',
            fields=[
                ('registrations_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.registrations')),
                ('statement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.statements')),
            ],
            options={
                'verbose_name': 'Hackathon Registration',
                'verbose_name_plural': 'Hackathon Registrations',
            },
            bases=('core.registrations',),
        ),
    ]
