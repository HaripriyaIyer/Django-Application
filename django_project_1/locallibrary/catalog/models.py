from django.db import models

# Create your models here.
class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=100, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta: 
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

class Keyword(models.Model):
    """Model representing a book genre."""
    keyword = models.CharField(max_length=200, help_text='Enter a book keyword (e.g. drug history)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.keyword

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    
    keyword_s = models.CharField(max_length=200,null=True)
    date = models.CharField(max_length=20,null=True)
    page = models.CharField(max_length=20,null=True)
    position = models.CharField(max_length=20,null=True)
    title = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    pages = models.CharField(max_length=20)
    publication_date = models.CharField(max_length=50)
    sales_rank = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13)
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
