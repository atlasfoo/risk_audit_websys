# Generated by Django 3.2.3 on 2021-05-30 15:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('risk', '0002_auto_20210530_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del control')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción del control')),
                ('order', models.IntegerField(verbose_name='Orden')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controls', to='risk.risk', verbose_name='Riesgo')),
            ],
            options={
                'verbose_name': 'Causa',
                'verbose_name_plural': 'Causas',
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='control',
            index=models.Index(fields=['risk', 'order'], name='controls_co_risk_id_218698_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='control',
            unique_together={('risk', 'order')},
        ),
    ]
