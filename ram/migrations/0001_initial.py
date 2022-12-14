# Generated by Django 4.0.6 on 2022-07-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllChars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('species', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('origin', models.JSONField(blank=True)),
                ('location', models.JSONField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('url', models.URLField(blank=True)),
                ('created', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('episode', models.IntegerField()),
                ('id_char', models.ManyToManyField(to='ram.allchars')),
            ],
        ),
    ]
