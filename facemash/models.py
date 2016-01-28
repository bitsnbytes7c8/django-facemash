from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):

    title = models.CharField(max_length=100);
    creator = models.ForeignKey(User, null=True);

    class meta:
        verbose_name_plural = 'Facemash game'

    def __unicode__(self):
        return self.title

class FaceMash(models.Model):
    """
    Model for facemash.
    The default values for ratings, rd (rating deviation) and
    sigma (volatility) are set as per suggested by the author
    of GLicko-2 algorithm.
    """

    game = models.ForeignKey(Game, null=True)
    name = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="facemash_photos")
    ratings = models.FloatField(default=1500)
    # rd = rating deviation
    rd = models.FloatField(default=350)
    # sigma is used as the expression for volatility
    sigma = models.FloatField(default=0.06)

    class Meta:
        verbose_name_plural = 'Facemash'

    def __unicode__(self):
        return self.name
