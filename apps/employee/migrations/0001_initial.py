# Generated by Django 4.2.4 on 2023-09-01 10:07

import apps.core.manager
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='Role')),
                ('joined_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created On')),
                ('dept', models.CharField(blank=True, max_length=50, null=True, verbose_name='Department')),
                ('reporting_to', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reporting To')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
                'ordering': ['-created_on'],
            },
            bases=('core.customuser',),
            managers=[
                ('user', apps.core.manager.UserManager()),
                ('objects', apps.core.manager.UserManager()),
            ],
        ),
    ]
