from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome


# ou, por exemplo, que apareça no titulo dos produtos, no admin do sistema Django, o nome seguido do estoque,
# escrevemos a str  (string) da seguinte forma:

#    def __str__(self):
#       return f'{self.nome} {self.estoque}'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('e-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
