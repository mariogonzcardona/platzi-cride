# Generated by Django 2.0.10 on 2020-05-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0003_auto_20200525_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='is_Active',
        ),
        migrations.AddField(
            model_name='membership',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Only active users are allowed to interact in the circle.', verbose_name='active status'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_admin',
            field=models.BooleanField(default=False, help_text="Circle admins can update the circle's data and manage its members.", verbose_name='circle admin'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='remaining_invitations',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='membership',
            name='used_invitations',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
