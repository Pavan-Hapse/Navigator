# Generated by Django 3.2.16 on 2022-12-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
