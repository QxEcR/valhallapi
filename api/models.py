from django.db import models

# Create your models here.


class Rank(models.Model):
    rankHolder = models.CharField(max_length=100)

    game = models.CharField(max_length=100)

    rank = models.CharField(max_length=100, default='NA')

    rankOrdered = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.rankHolder} - {self.game} - {self.rank}"
