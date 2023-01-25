# Generated by Django 4.1.4 on 2023-01-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'pro',
            },
        ),
    ]
