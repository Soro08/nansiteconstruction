# Generated by Django 2.2.5 on 2019-10-08 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lieu',
                'verbose_name_plural': 'Lieux',
            },
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Specialite',
                'verbose_name_plural': 'Specialites',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=30, null=True)),
                ('status', models.BooleanField(default=False)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('lieu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lieu_etudiant', to='bootcamp.Lieu')),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etudiant_specialité', to='bootcamp.Specialite')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='etudiant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Etudiant',
                'verbose_name_plural': 'Etudiants',
            },
        ),
        migrations.CreateModel(
            name='Encadreur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encadreur_specialite', to='bootcamp.Specialite')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='encadreur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encadreur',
                'verbose_name_plural': 'Encadreurs',
            },
        ),
    ]