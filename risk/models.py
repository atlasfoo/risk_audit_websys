from ckeditor.fields import RichTextField
from django.db import models


class Risk(models.Model):
    """Represents a risk in the organization's risk matrix"""
    name = models.CharField(verbose_name="Nombre del riesgo", max_length=100)
    description = RichTextField(verbose_name="Descripción del riesgo")

    class Meta:
        verbose_name = "Riesgo"
        verbose_name_plural = "Riesgos"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Cause(models.Model):
    """Represents a risk causes in the risk matrix"""
    name = models.CharField(verbose_name="Nombre de la causa", max_length=100)
    description = RichTextField(verbose_name="Descripción de la causa")
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, verbose_name="Riesgo", related_name="causes")

    class Meta:
        verbose_name = "Causa"
        verbose_name_plural = "Causas"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Effect(models.Model):
    """Represents a risk effects in the risk matrix"""
    name = models.CharField(verbose_name="Nombre de la consecuencia", max_length=100)
    description = RichTextField(verbose_name="Descripción de la consecuencia")
    economic_loss = models.DecimalField(verbose_name="Costo económico", decimal_places=2, max_digits=16)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, verbose_name="Riesgo", related_name="effects")

    class Meta:
        verbose_name = "Consecuencia"
        verbose_name_plural = "Consecuencias"
        ordering = ["id"]

    def __str__(self):
        return self.name
