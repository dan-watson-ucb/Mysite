from django.db import models
from datetime import datetime

# Create your models here.
# Creates a new table called Tutorial and these are our columns
class Article(models.Model): #inherits from Model
    Article_title = models.CharField(max_length= 200)
    Article_slug = models.CharField(max_length = 300)
    Article_content = models.TextField()
    Article_image = models.ImageField(blank = True, null=True)
    Article_published = models.DateTimeField("date published",
                                               default = datetime.now()) # what we're calling it

    def __str__(self):
        return self.Article_title