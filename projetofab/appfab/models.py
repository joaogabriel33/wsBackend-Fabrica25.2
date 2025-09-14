from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    TIPOS = (
        ('carro', 'Carro'),
        ('moto', 'Moto'),
    )
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    ano = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="veiculos")

    def __str__(self):
        return f"{self.nome} ({self.marca.nome})"