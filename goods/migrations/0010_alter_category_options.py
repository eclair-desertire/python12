# Generated by Django 5.0.1 on 2024-02-07 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_good_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pk',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
