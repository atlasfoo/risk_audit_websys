from ckeditor.fields import RichTextField
from django.db import models

from risk.models import Risk


class Control(models.Model):
    name = models.CharField(verbose_name="Nombre del control", max_length=100,
                            null=False, blank=False)
    description = RichTextField(verbose_name="Descripción del control",
                                null=False, blank=False)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, verbose_name="Riesgo", related_name="controls",
                             null=False)
    order = models.IntegerField(verbose_name="Orden", null=False)

    class Meta:
        unique_together = (('risk', 'order'),)
        indexes = [
            models.Index(fields=['risk', 'order'])
        ]
        verbose_name = "Causa"
        verbose_name_plural = "Causas"
        ordering = ["id"]

    def __str__(self):
        return self.name
