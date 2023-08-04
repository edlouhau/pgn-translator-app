from django.db import models

# Create your models here.

class Game(models.Model):
    game = models.CharField(max_length=200)
    translated_pgn = models.CharField(max_length=200, blank=True)
    
    
    def __str__(self):
        return self.game

