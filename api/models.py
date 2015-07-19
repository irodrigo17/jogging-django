from django.db import models
from django.contrib.auth.models import User


class Jog(models.Model):

    user = models.ForeignKey(User)
    date = models.DateTimeField(db_index=True)
    meters = models.FloatField()
    seconds = models.FloatField()

    def __str__(self):
        return '{user}, {date}'.format(user=str(self.user), date=self.date)

    def average_speed(self):
        return self.meters / self.seconds
