# Generated by Django 4.0.6 on 2022-08-28 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_rename_describ_project_describtion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='describtion',
            new_name='description',
        ),
    ]
