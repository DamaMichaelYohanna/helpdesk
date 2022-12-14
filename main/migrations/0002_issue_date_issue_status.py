# Generated by Django 4.1.3 on 2022-11-18 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='date',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Resolved', 'Resolved'), ('Failed', 'Failed')], default='Pending', max_length=15),
            preserve_default=False,
        ),
    ]
