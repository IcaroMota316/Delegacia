from django.db import models

class Policial(models.Model):
    nome = models.CharField(max_length=100)
    patente = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.patente} {self.nome}"

class Ocorrencia(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=150)
    policial_responsavel = models.ForeignKey(Policial, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} - {self.local}"

class Vitima(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    contato = models.CharField(max_length=20)
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, related_name='vitimas')

    def __str__(self):
        return self.nome

class Suspeito(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('Preso', 'Preso'), ('Foragido', 'Foragido')],
        default='Foragido'
    )
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, related_name='suspeitos')

    def __str__(self):
        return self.nome

class Evidencia(models.Model):
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='evidencias/', blank=True, null=True)
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, related_name='evidencias')

    def __str__(self):
        return f"Evidência da ocorrência {self.ocorrencia.id}"
    
class Suspeito(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

