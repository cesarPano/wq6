# Generated by Django 3.0.6 on 2020-05-20 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Desf', '0001_initial'),
        ('TRevi', '0001_initial'),
        ('Tecn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de revisión')),
                ('hora', models.TimeField(verbose_name='Hora de revisión')),
                ('desf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Desf.Desf', verbose_name='Desfibrilador')),
                ('tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tecn.Tecn', verbose_name='Técnico')),
                ('trevi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRevi.Trevi', verbose_name='Tipo de revisión')),
            ],
            options={
                'verbose_name': 'revi',
                'verbose_name_plural': 'revis',
            },
        ),
    ]
