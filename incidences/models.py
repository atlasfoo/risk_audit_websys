from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from controls.models import Control
from risk.models import Risk, Cause, Effect


class Incidence(models.Model):
    name = models.CharField(verbose_name="Nombre del control", max_length=100,
                            null=False, blank=False)
    description = RichTextField(verbose_name="Descripción del control",
                                null=False, blank=False)
    date_of_occurrence = models.DateTimeField(verbose_name="Fecha y hora del suceso", auto_now_add=True)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, verbose_name="Riesgo", related_name="incidences",
                             null=False)
    causes = models.ManyToManyField(Cause, verbose_name="Causas presentes", related_name="incidences",
                                   related_query_name="incidence")
    effects = models.ManyToManyField(Effect, verbose_name="Consencuencias efectivas", related_name='incidences',
                                     related_query_name='incidence')
    controls = models.ManyToManyField(Control, verbose_name="Controles Aplicados", related_name='incidences',
                                     related_query_name='incidence')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario registrador", related_name="+")

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ["id"]

    def __str__(self):
        return self.name
