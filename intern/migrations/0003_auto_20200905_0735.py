# Generated by Django 3.1.1 on 2020-09-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_auto_20200904_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='Password',
            field=models.TextField(default='pass'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Password',
            field=models.TextField(default='pass'),
            preserve_default=False,
        ),
    ]