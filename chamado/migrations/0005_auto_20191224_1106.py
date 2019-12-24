# Generated by Django 3.0.1 on 2019-12-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0004_auto_20191224_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('ABERTO', 'Aberto'), ('EM_ANDAMENTO', 'Em andamento'), ('AGUARDANDO', 'Aguardando'), ('CONCLUIDO', 'Concluido')], default='Aberto', max_length=20),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='tipo_chamado',
            field=models.CharField(choices=[('INCIDENTE', 'Incidente'), ('REQUISICAO', 'Requsição')], default='Incidente', max_length=20),
        ),
    ]
