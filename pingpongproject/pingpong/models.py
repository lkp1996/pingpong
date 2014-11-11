from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    player_one = models.ForeignKey(Player, related_name='games_as_p1')
    player_two = models.ForeignKey(Player, related_name='games_as_p2')
    score_one = models.IntegerField()
    score_two = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey(Player, related_name='games_as_winner')

    def save(self, *args, **kwargs):
        if self.score_one > self.score_two:
            self.winner = self.player_one
        else:
            self.winner = self.player_two
        super(Game, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{0} vs {1} score: {2} - {3} date: {4}".format(
            self.player_one, self.player_two, self.score_one, self.score_two,
            self.created
            )
