from django.db import models


class Desf(models.Model):
    tdesf = models.ForeignKey(
        "TDesf.Tdesf",
        on_delete=models.CASCADE,
        verbose_name="Tipo de desfibrilador",
    )
    localizacion = models.CharField(
        max_length=100,
        verbose_name="Ubicación",
    )
    responsable = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Persona responsable",
    )
    imagen = models.ImageField(
        upload_to="desfs",
        null=True,
        blank=True,
        verbose_name="Imagen o foto",
    )

    def __str__(self):
        return self.localizacion

    class Meta:
        verbose_name = "desf"
        verbose_name_plural = "desfs"
