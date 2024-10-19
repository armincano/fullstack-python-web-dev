from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        permissions = (
            ('development', 'Can do development'),
            ('scrum_master', 'Can do scrum master'),
            ('product_owner', 'Can do product owner'),
        )
    
    def __str__(self):
        return self.title
