# Generated by Django 2.2.2 on 2019-09-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lazer', '0005_esportes_disponiveis'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Esportes_disponiveis',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='aluno',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]
