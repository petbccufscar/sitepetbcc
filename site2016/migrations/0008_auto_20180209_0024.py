# Generated by Django 2.0.2 on 2018-02-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site2016', '0007_auto_20180208_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapaps',
            name='data_resultado',
            field=models.DateField(null=True, verbose_name='data do resultado'),
        ),
        migrations.AddField(
            model_name='processoseletivo',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='PS ativo'),
        ),
        migrations.AlterField(
            model_name='processoseletivo',
            name='requisitos',
            field=models.TextField(default=' <li value="a)">Ser aluno regularmente matriculado no curso de Bacharelado em Ciência da Computação e estar cursando a partir do 2º (segundo) semestre de graduação; </li>\n<li value="b)">Apresentar média ponderada semestral geral maior ou igual a 6.0 (seis);</li>\n<li value="c)">Ter disponibilidade para se dedicar 20 (vinte) horas semanais nas atividadesdo programa;</li>', verbose_name='requisitos'),
        ),
        migrations.AlterUniqueTogether(
            name='processoseletivo',
            unique_together={('ano', 'semestre')},
        ),
    ]
