from django.db import models
from datetime import datetime

# Create your models here.
# Creates a new table called Tutorial and these are our columns
class Article(models.Model): #inherits from Model
    article_title = models.CharField(max_length= 200)
    article_slug = models.CharField(max_length = 300)
    article_content = models.TextField()
    article_image = models.ImageField(blank = True, null=True)
    article_published = models.DateTimeField("date published",
                                               default = datetime.now()) # what we're calling it

    def __str__(self):
        return self.article_title

class Players(models.Model):
    player_name = models.CharField(max_length=300, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'players'

