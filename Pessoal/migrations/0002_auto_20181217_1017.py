# Generated by Django 2.1.4 on 2018-12-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados_base',
            name='data_diac',
            field=models.CharField(default=1, max_length=100, verbose_name='Data da Profissão Diaconal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_base',
            name='data_perpetua',
            field=models.CharField(default=1, max_length=100, verbose_name='Data da Profissão Religiosa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_base',
            name='data_presb',
            field=models.CharField(default=1, max_length=100, verbose_name='Data da Profissão Presbiteral'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_base',
            name='formacao',
            field=models.CharField(default=1, max_length=100, verbose_name='Data da Profissão Presbiteral'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_base',
            name='local_diac',
            field=models.CharField(default=1, max_length=100, verbose_name='Local da Profissão Diaconal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_base',
            name='local_perpetua',
            field=models.CharField(default=1, max_length=100, verbose_name='Local da Profissão Religiosa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dados_base',
            name='local_presb',
            field=models.CharField(default=1, max_length=100, verbose_name='Local da Profissão Presbiteral'),
            preserve_default=False,
        ),
    ]
