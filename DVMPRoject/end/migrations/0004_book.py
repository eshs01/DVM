# Generated by Django 5.1.5 on 2025-02-09 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('end', '0003_rename_borading_bus_boarding'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookseats', models.IntegerField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='end.bus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uzer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
