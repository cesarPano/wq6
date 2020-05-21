from django.db import models


class Tecn(models.Model):
    tnombre = models.CharField(
        max_length=100,
        verbose_name="Técnico",
    )

    def __str__(self):
        return self.tnombre

    class Meta:
        verbose_name = "tecn"
        verbose_name_plural = "tecns"
