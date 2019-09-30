# Generated by Django 2.2.5 on 2019-09-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=10)),
                ('manas', models.ManyToManyField(to='mana.Mana')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
    ]
