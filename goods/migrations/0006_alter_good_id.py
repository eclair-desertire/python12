# Generated by Django 5.0.1 on 2024-02-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_good_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
