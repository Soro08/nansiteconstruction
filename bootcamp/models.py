from django.db import models
from django.contrib.auth.models import User

class Lieu(models.Model):
    """Model definition for Lieu."""
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Lieu."""

        verbose_name = 'Lieu'
        verbose_name_plural = 'Lieux'

    def __str__(self):
        """Unicode representation of Lieu."""
        return '{}'.format(self.name) 


class Specialite(models.Model):
    """Model definition for Specialite."""
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Specialite."""

        verbose_name = 'Specialite'
        verbose_name_plural = 'Specialites'

    def __str__(self):
        """Unicode representation of Specialite."""
        return '{}'.format(self.name )


class Encadreur(models.Model):
    """Model definition for Encadreur."""
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='encadreur')
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,related_name='encadreur_specialite')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for Encadreur."""
        verbose_name = 'Encadreur'
        verbose_name_plural = 'Encadreurs'

    def __str__(self):
        """Unicode representation of Encadreur."""
        return '{}'.format(self.user) 

class Etudiant(models.Model):
    """Model definition for Etudiant."""
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='etudiant')
    contact = models.CharField(max_length=30,null=True)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,related_name='etudiant_specialité')
    lieu = models.ForeignKey(Lieu,on_delete=models.SET_NULL,related_name='lieu_etudiant',null=True)
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Etudiant."""

        verbose_name = 'Etudiant'
        verbose_name_plural = 'Etudiants'

    def __str__(self):
        """Unicode representation of Etudiant."""
        return '{}'.format(self.user) # TODO

