# Generated by Django 3.0.2 on 2021-03-01 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='vaccine_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vaccine.VaccineGroups'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='vaccine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vaccine.Vaccine'),
        ),
    ]