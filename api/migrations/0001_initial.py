# Generated by Django 4.0.3 on 2022-03-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rankHolder', models.CharField(max_length=100)),
                ('game', models.CharField(max_length=100)),
                ('rank', models.CharField(default='NA', max_length=100)),
                ('ordered', models.IntegerField(default=5)),
            ],
        ),
    ]
