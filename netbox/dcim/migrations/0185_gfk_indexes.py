# Generated by Django 4.2.7 on 2023-12-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dcim', '0184_protect_child_interfaces'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='cabletermination',
            index=models.Index(fields=['termination_type', 'termination_id'], name='dcim_cablet_termina_884752_idx'),
        ),
        migrations.AddIndex(
            model_name='inventoryitem',
            index=models.Index(fields=['component_type', 'component_id'], name='dcim_invent_compone_0560bb_idx'),
        ),
        migrations.AddIndex(
            model_name='inventoryitemtemplate',
            index=models.Index(fields=['component_type', 'component_id'], name='dcim_invent_compone_77b5f8_idx'),
        ),
    ]
