# Generated by Django 2.2.5 on 2019-10-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='specialite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etudiant_specialiteS', to='bootcamp.Specialite'),
        ),
    ]
