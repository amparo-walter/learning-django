from turtle import title
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'