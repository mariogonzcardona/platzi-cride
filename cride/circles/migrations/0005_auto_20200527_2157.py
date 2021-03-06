# Generated by Django 2.0.10 on 2020-05-27 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('circles', '0004_auto_20200525_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('used_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='circle',
            name='is_limited',
            field=models.BooleanField(default=False, help_text='Limited circles can grow up to a fixed number of members.', verbose_name='limited'),
        ),
        migrations.AlterField(
            model_name='circle',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Public circles are listed in the main page so everyone know about their existence.'),
        ),
        migrations.AlterField(
            model_name='circle',
            name='verified',
            field=models.BooleanField(default=False, help_text='Verified circles are also known as official communities.', verbose_name='verified circle'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='circle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circles.Circle'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='issued_by',
            field=models.ForeignKey(help_text='Circle member that is providing the invitation', on_delete=django.db.models.deletion.CASCADE, related_name='issued_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='used_by',
            field=models.ForeignKey(help_text='User that used the code to enter the circle', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
