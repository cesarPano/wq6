from django.db import models


class Trevi(models.Model):
    trevi = models.CharField(
        max_length=20,
        verbose_name="Tipo de revisión",
    )

    def __str__(self):
        return self.trevi

    class Meta:
        verbose_name = "trevi"
        verbose_name_plural = "trevis"
