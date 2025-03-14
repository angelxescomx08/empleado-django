from django.db import models


# Create your models here.
class Departamento(models.Model):
    # nombre del campo en el admin
    name = models.CharField("Nombre", max_length=50, blank=True, null=True)
    short_name = models.CharField("Nombre corto", max_length=20, unique=True)
    anulate = models.BooleanField("Anulado", default=False)

    # Se usa hacer cosas en el administrador de django en ese modelo
    # Se puede cambiar como se muestra el nombre del modelo en el admin
    class Meta:
        # Pone el nombre del modelo en el admin
        verbose_name = "Mi departamento"
        # Pone el nombre del modelo en plural en el admin
        verbose_name_plural = "Mis departamentos"
        # Ordena los campos en el admin por el nombre descendente (abecedario)
        ordering = ["-name"]
        # Hace que no pueda haber una combinación de nombre y short_name repetida
        unique_together = ("name", "short_name")

    def __str__(self) -> str:
        return str(self.id) + "-" + self.name + "-" + self.short_name
