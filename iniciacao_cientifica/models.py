from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome do Autor')

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores" 

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título', help_text="Informe o Título completo.")
    authors = models.ManyToManyField(Author, verbose_name='Autor')
    abstract = models.TextField(verbose_name='Resumo')    
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Publicação')
    event = models.CharField(max_length=250, verbose_name='Evento')

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def get_authors(self):
        return ",".join([str(a) for a in self.authors.all()])

    def __str__(self):
        return "{0}".format(self.title, self.authors, self.abstract, self.event)


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome Completo')
    username = models.CharField(max_length=200, verbose_name='Nome de Usuário')
    institution = models.CharField(max_length=100, verbose_name='Instituição')
    article = models.ManyToManyField(Article, verbose_name='Artigos', blank=True, null=True)
    areasofinterest = models.CharField(max_length=200, verbose_name='Área de Interesse')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def get_articles(self):
        return ",".join([str(a) for a in self.article.all()])

    def __str__(self):
        return "{0}".format(self.name, self.username, self.article)







