# Generated by Django 5.0.1 on 2024-02-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_good_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]