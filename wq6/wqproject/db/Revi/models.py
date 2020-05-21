from django.db import models


class Revi(models.Model):
    desf = models.ForeignKey(
        "Desf.Desf",
        on_delete=models.CASCADE,
        verbose_name="Desfibrilador",
    )
    tecnico = models.ForeignKey(
        "Tecn.Tecn",
        on_delete=models.CASCADE,
        verbose_name="Técnico",
    )
    trevi = models.ForeignKey(
        "TRevi.Trevi",
        on_delete=models.CASCADE,
        verbose_name="Tipo de revisión",
    )
    fecha = models.DateField(
        verbose_name="Fecha de revisión",
    )
    hora = models.TimeField(
        verbose_name="Hora de revisión",
    )

    def __str__(self):
        return self.desf.localizacion

    class Meta:
        verbose_name = "revi"
        verbose_name_plural = "revis"
