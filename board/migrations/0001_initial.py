# Generated by Django 4.0.5 on 2022-06-08 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booktbl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('rule', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.CharField(blank=True, max_length=10, null=True)),
                ('img', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'booktbl',
                'managed': False,
            },
        ),
    ]