from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ('blue' , 'Blue'),
        ('green' , 'Green'),
        ('yellow' , 'Yellow')
    )
    #name , slug , bg_color
    name = models.CharField( max_length=50)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50 , choices=BG_CHOICES)

    def __str__(self)->str:
        return self.name
    
class Link(models.Model):
    #text , url , profile
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name='links')

    def __str__(self):
        return f"{self.text} | {self.url} | {self.profile}"
