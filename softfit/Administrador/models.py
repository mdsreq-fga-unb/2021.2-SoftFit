from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Usuario(models.Model):
    idu = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        abstract = True

class AvaliacaoFisica(models.Model):
    peso = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5, )
    altura = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5)
    imc = models.DecimalField(decimal_places=2, max_digits=5)
    braco_d = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5)
    perna_e = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5) 
    cintura = models.DecimalField(blank=False , null = False,decimal_places=2, max_digits=5)
    comentario_af = models.CharField(max_length=500)

class EstadoFinanceiro(models.Model):

    STATUS = (
        ('Em Dia', 'Em Dia'),
        ('Inadimplente', 'Inadimplente'),
    )

    condicao = models.CharField(
        max_length=12,
        choices=STATUS,
    )

class Objetivo(models.Model):

    OBJS = (
        ('A Selecionar', 'A Selecionar'),
        ('Ganhar massa muscular', 'Ganhar massa muscular'),
        ('Emagrecer', 'Emagrecer'),
        ('Ganhar resistência', 'Ganhar resistência'),
    )

    opcao = models.CharField(
        max_length=21,
        choices=OBJS,
    )

    comentario = models.CharField(max_length=500)

class Aluno(Usuario): 
    avaliacao = models.ForeignKey(AvaliacaoFisica, on_delete=models.CASCADE)
    estadof = models.ForeignKey(EstadoFinanceiro, on_delete=models.CASCADE, null=True)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    frequencia = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Professor(Usuario):
    segunda_manha = models.BooleanField(default=False)
    segunda_tarde = models.BooleanField(default=False)
    segunda_noite = models.BooleanField(default=False)

    terca_manha = models.BooleanField(default=False)
    terca_tarde = models.BooleanField(default=False)
    terca_noite = models.BooleanField(default=False)

    quarta_manha = models.BooleanField(default=False)
    quarta_tarde = models.BooleanField(default=False)
    quarta_noite = models.BooleanField(default=False)

    quinta_manha = models.BooleanField(default=False)
    quinta_tarde = models.BooleanField(default=False)
    quinta_noite = models.BooleanField(default=False)

    sexta_manha = models.BooleanField(default=False)
    sexta_tarde = models.BooleanField(default=False)
    sexta_noite = models.BooleanField(default=False)

    sabado_manha = models.BooleanField(default=False)
    sabado_tarde = models.BooleanField(default=False)

    domingo_manha = models.BooleanField(default=False)

    def __str__(self):
        return self.nome