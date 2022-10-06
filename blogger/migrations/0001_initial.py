# Generated by Django 4.0.6 on 2022-07-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(default='', max_length=70)),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
