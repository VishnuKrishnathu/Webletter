# Generated by Django 4.0 on 2022-01-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0005_alter_customuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
