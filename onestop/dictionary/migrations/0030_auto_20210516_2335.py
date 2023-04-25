# Generated by Django 3.2 on 2021-05-16 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0029_alter_oshindongaword_word_phonetics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaloshindongaword',
            name='word_phonetics',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.oshindongaphonetic'),
        ),
        migrations.AlterField(
            model_name='oshindongaword',
            name='word_phonetics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dictionary.oshindongaphonetic'),
        ),
    ]
