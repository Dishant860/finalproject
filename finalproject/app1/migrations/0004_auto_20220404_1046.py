# Generated by Django 2.1.5 on 2022-04-04 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20220404_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
