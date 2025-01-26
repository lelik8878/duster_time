from django.db import models

class DusterTime(models.Model):
    duster_time = models.DateTimeField(verbose_name='Duster Time')

    class Meta:
        verbose_name = 'Время дастера'
        verbose_name_plural = 'Время дастеров'

    def __str__(self):
        return str(self.duster_time)
