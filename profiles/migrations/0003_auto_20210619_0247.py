# Generated by Django 3.1.1 on 2021-06-19 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
