# Generated by Django 4.0.6 on 2022-07-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_blogcomment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='image',
            field=models.ImageField(default='', upload_to='Icoder/static/img'),
        ),
    ]
