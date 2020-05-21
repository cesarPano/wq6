from django.db import models


class Tran(models.Model):
    desf = models.ForeignKey(
        "Desf.Desf",
        on_delete=models.CASCADE,
        verbose_name="Desfibrilador",
    )
    fecha = models.DateField(
        verbose_name="Fecha de transmisión",
    )
    hora = models.TimeField(
        verbose_name="Hora de transmisión",
    )
    imagen = models.CharField(
        max_length=100,
        verbose_name="Texto transmitido",
    )

    def __str__(self):
        return self.desf.localizacion

    class Meta:
        verbose_name = "tran"
        verbose_name_plural = "trans"
