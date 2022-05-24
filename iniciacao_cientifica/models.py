from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome Completo')
    username = models.CharField(max_length=200, verbose_name='Nome de Usuário')
    institution = models.CharField(max_length=100, verbose_name='Instituição')
    areasofinterest = models.CharField(max_length=200, verbose_name='Área de Interesse')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')


    def __str__(self):
        return self.name 

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título', help_text="Informe o Título completo.")
    authors = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Autor')
    abstract = models.TextField(verbose_name='Resumo')    
    pub_date = models.DateTimeField(verbose_name='Data de Publicação')
    event = models.CharField(max_length=250, verbose_name='Evento')


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title






