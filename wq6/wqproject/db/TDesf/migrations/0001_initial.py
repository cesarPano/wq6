# Generated by Django 3.0.6 on 2020-05-20 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tdesf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdesf', models.CharField(max_length=10, verbose_name='Tipo de desfibrilador')),
            ],
            options={
                'verbose_name': 'tdesf',
                'verbose_name_plural': 'tdesfs',
            },
        ),
    ]