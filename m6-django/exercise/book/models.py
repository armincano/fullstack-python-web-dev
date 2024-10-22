from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    rating = models.IntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        permissions = (
            ('development', 'Can do development'),
            ('scrum_master', 'Can do scrum master'),
            ('product_owner', 'Can do product owner'),
        )
    
    def __str__(self):
        return self.title
