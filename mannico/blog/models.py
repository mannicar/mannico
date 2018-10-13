from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    title       = models.CharField(max_length=100, help_text="Article Title")
    author      = models.CharField(max_length=50, help_text="Article Author")
    pub_date    = models.DateTimeField(default=datetime.utcnow())
    body        = models.TextField()

