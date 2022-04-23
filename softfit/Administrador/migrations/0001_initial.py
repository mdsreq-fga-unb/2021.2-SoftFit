# Generated by Django 4.0.3 on 2022-04-19 16:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, 'O valor deve ser maior que 0'), django.core.validators.MaxValueValidator(250)])),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, 'O valor deve ser maior que 0'), django.core.validators.MaxValueValidator(250)])),
                ('imc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('braco_d', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, 'O valor deve ser maior que 0'), django.core.validators.MaxValueValidator(400)])),
                ('perna_e', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, 'O valor deve ser maior que 0'), django.core.validators.MaxValueValidator(400)])),
                ('cintura', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0, 'O valor deve ser maior que 0'), django.core.validators.MaxValueValidator(400)])),
                ('comentario_af', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoFinanceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicao', models.CharField(choices=[('Em Dia', 'Em Dia'), ('Inadimplente', 'Inadimplente')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.CharField(choices=[('A Selecionar', 'A Selecionar'), ('Ganhar massa muscular', 'Ganhar massa muscular'), ('Emagrecer', 'Emagrecer'), ('Ganhar resistência', 'Ganhar resistência')], max_length=21)),
                ('comentario', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('segunda_manha', models.BooleanField(default=False)),
                ('segunda_tarde', models.BooleanField(default=False)),
                ('segunda_noite', models.BooleanField(default=False)),
                ('terca_manha', models.BooleanField(default=False)),
                ('terca_tarde', models.BooleanField(default=False)),
                ('terca_noite', models.BooleanField(default=False)),
                ('quarta_manha', models.BooleanField(default=False)),
                ('quarta_tarde', models.BooleanField(default=False)),
                ('quarta_noite', models.BooleanField(default=False)),
                ('quinta_manha', models.BooleanField(default=False)),
                ('quinta_tarde', models.BooleanField(default=False)),
                ('quinta_noite', models.BooleanField(default=False)),
                ('sexta_manha', models.BooleanField(default=False)),
                ('sexta_tarde', models.BooleanField(default=False)),
                ('sexta_noite', models.BooleanField(default=False)),
                ('sabado_manha', models.BooleanField(default=False)),
                ('sabado_tarde', models.BooleanField(default=False)),
                ('domingo_manha', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('frequencia', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador.avaliacaofisica')),
                ('estadof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Administrador.estadofinanceiro')),
                ('objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador.objetivo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
