# Generated by Django 2.2.4 on 2020-02-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100, verbose_name='field1')),
                ('field2', models.CharField(max_length=100, verbose_name='field2')),
            ],
        ),
    ]
