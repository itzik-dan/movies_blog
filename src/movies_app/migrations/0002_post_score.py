# Generated by Django 3.0.3 on 2020-02-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.DecimalField(decimal_places=1, default=9.1, max_digits=2),
            preserve_default=False,
        ),
    ]
