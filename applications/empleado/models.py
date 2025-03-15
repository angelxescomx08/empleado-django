from django.db import models

from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return str(self.id) + "" + self.habilidad


# Create your models here.
class Empleado(models.Model):
    JOB_CHOICES = (
        ("0", "CONTADOR"),
        ("1", "ADMINISTRADOR"),
        ("2", "ECONOMISTA"),
        ("3", "OTRO"),
    )
    first_name = models.CharField("Nombre", max_length=60)
    last_name = models.CharField("Apellido", max_length=60)
    job = models.CharField("Trabajo", max_length=60, choices=JOB_CHOICES)
    departament = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(
        "Imagen", upload_to="empleado/imagenes/", blank=True, null=True
    )
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self) -> str:
        return str(self.id) + "-" + self.first_name + " " + self.last_name
