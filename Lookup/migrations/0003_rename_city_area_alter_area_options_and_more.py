# Generated by Django 4.2.4 on 2023-08-21 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lookup', '0002_rename_country_city_alter_city_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='Area',
        ),
        migrations.AlterModelOptions(
            name='area',
            options={},
        ),
        migrations.RenameField(
            model_name='code',
            old_name='city',
            new_name='area',
        ),
    ]