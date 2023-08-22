# Generated by Django 4.2.4 on 2023-08-21 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lookup', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='City',
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.RenameField(
            model_name='code',
            old_name='country',
            new_name='city',
        ),
    ]