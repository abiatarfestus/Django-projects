# Generated by Django 3.1.1 on 2021-02-26 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0017_auto_20210226_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalworddefinition',
            old_name='plural3',
            new_name='synonym1',
        ),
        migrations.RenameField(
            model_name='worddefinition',
            old_name='plural3',
            new_name='synonym1',
        ),
        migrations.RemoveField(
            model_name='historicalworddefinition',
            name='plural',
        ),
        migrations.RemoveField(
            model_name='historicalworddefinition',
            name='tense',
        ),
        migrations.RemoveField(
            model_name='historicalworddefinition',
            name='variants',
        ),
        migrations.RemoveField(
            model_name='worddefinition',
            name='plural',
        ),
        migrations.RemoveField(
            model_name='worddefinition',
            name='tense',
        ),
        migrations.RemoveField(
            model_name='worddefinition',
            name='variants',
        ),
    ]
