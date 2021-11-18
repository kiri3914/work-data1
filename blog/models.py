from django.db import models


class Persons(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    email = models.EmailField(verbose_name='Email')
    data = models.DateField(verbose_name='Date')
    record = models.CharField(verbose_name='Record', max_length=255)
    location = models.CharField(verbose_name='Location', max_length=255)
    best_song = models.CharField(verbose_name='Best Song', max_length=255)
    actions = models.BooleanField(default=True, verbose_name='Action')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Persons'
        verbose_name_plural = 'Person'
