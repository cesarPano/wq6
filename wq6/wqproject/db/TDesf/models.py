from django.db import models


class Tdesf(models.Model):
    tdesf = models.CharField(
        max_length=10,
        verbose_name="Tipo de desfibrilador",
    )

    def __str__(self):
        return self.tdesf

    class Meta:
        verbose_name = "tdesf"
        verbose_name_plural = "tdesfs"
