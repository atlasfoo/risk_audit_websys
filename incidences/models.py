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
    cause = models.ManyToManyField(Cause, verbose_name="Causas presentes", related_name="incidences",
                                   related_query_name="incidence")
    effects = models.ManyToManyField(Effect, verbose_name="Consencuencias efectivas", related_name='incidences',
                                     related_query_name='incidence')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario registrador", related_name="+")

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        ordering = ["id"]

    def __str__(self):
        return self.name


class IncidenceControl(models.Model):
    """Manual m2m bw Incidences and Controls for was_effective flag mark"""
    incidence = models.ForeignKey(Incidence, on_delete=models.CASCADE, verbose_name="Incidencia",
                                  related_name="controls", null=False)
    control = models.ForeignKey(Control, on_delete=models.CASCADE, verbose_name="Control", related_name="incidences",
                                null=False)
    was_effective = models.BooleanField(default=False, verbose_name="Control fue efectivo?")

    class Meta:
        unique_together = (('id', 'incidence', 'control'),)
        indexes = [
            models.Index(fields=['id', 'incidence', 'control'])
        ]
        verbose_name = "Efectividad del control en la incidencia"
        verbose_name_plural = "Efectividad de los controles en la incidencia"
        ordering = ["id"]
