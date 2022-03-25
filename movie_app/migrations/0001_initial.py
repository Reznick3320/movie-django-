# Generated by Django 4.0.3 on 2022-03-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('rating', models.IntegerField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('budget', models.IntegerField(default=1000000)),
            ],
        ),
    ]
