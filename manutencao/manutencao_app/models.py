from django.db import models

# Create your models here.

class Escada(models.Model):
    codigo = models.CharField(max_length=20)
    data_envio = models.DateField()
    altura = models.IntegerField(default=0)
    problema = models.CharField(max_length=100)

    STATUS_CHOICE = [
        ('pendente', 'Pendente'),
        ('em_manutencao', 'Em manutenção'),
        ('concluida', 'Concluída'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pendente')

    def __str__(self):
        return self.codigo