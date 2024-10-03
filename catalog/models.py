from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

# Parte 3:Definindo os modelos LocalLiterary Consulte as descriçoes dos campos 

class Genre(models.Model):
    # representa um genero literario
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction)")

    def __str__(self):
        # String para representação do objeto
        return self.name

# Modelo de representação de um livro (mas não uma copia especifica de um livro)
class Book(models.Model):
    title = models.CharField(max_length=200)
    #Chave estrangeira usada, porque um livro   pode ter um autor, mas um autor pode ter varios livros
    # Autor como string em vez de objeto porque ele ainda n o foi declarado nesse arquivo
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Digite uma breve descricão do livro')

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField usado porque um genero pode conter muitos livros. Livros podem abranger muitos generos.
    # A classe Genre ja foi definida, portanto podemos especificar o objeto acima.

    genre = models.ManyToManyField(Genre, help_text='Selecione um genero para este livro')

    #String para representação do objeto
    def __str__(self):
        return self.title

    #Retorna um URL para acessar uma instância desta classe.
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])

class BookInstance(models.Model):
    # O modelo representa uma copia de um livro (por exemplo, de um livro emprestado para um leitor).
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico para este exemplar')

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    imprint = models.CharField(max_length=200)

    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Manutenção'),
        ('o', 'Emprestado'),
        ('a', 'Disponivel'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1, 
        choices=LOAN_STATUS, 
        blank=True, 
        default='m', 
        help_text='Disponibilidade do Livro'
        )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
#Modelo para representar um Autor.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'