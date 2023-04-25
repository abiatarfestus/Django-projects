# Generated by Django 3.1.1 on 2021-02-02 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionary', '0002_auto_20210202_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_of_speech', models.CharField(choices=[('Noun', 'Noun'), ('Pron.', 'Pronoun'), ('Verb', 'Verb'), ('Adj.', 'Adjective'), ('Adv.', 'Adverb'), ('Prep.', 'Preposition'), ('Conj.', 'Conjunction'), ('Int.', 'Interjection')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='OshindongaWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateField(auto_now_add=True)),
                ('time_modified', models.DateField(auto_now=True)),
                ('word', models.CharField(max_length=50)),
                ('english_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.englishword')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalOshindongaWord',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('time_added', models.DateField(blank=True, editable=False)),
                ('time_modified', models.DateField(blank=True, editable=False)),
                ('history_change_reason', models.TextField(null=True)),
                ('word', models.CharField(max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('english_word', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dictionary.englishword')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical oshindonga word',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
