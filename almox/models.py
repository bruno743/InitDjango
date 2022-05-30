from django.db import models

# Create your models here.
class Loc(models.Model):
    loc_name = models.CharField(max_length=255)
    loc_addrss = models.TextField()

    def __str__(self):
        return self.loc_name

class Mod(models.Model):
    mod_brand = models.CharField(max_length=120)
    mod_model = models.CharField(max_length=120)
    mod_description = models.TextField()

    def __str__(self):
        return self.mod_model

class Type(models.Model):
    type_desc = models.CharField(max_length=120)

    def __str__(self):
        return self.type_desc

class Comp(models.Model):

    STATUS_CHOICES = (
        ('operante', 'O'),
        ('inoperante', 'I'),
    )

    ESTADO_CHOICES = (
        ('disponivel/com caixa', 'DC'),
        ('disponivel/sem caixa', 'DS'),
        ('indisponivel', 'IND'),
        ('cedido', 'C'),
    )

    comp_name = models.CharField(max_length=255)
    comp_mod = models.ForeignKey(Mod, on_delete=models.CASCADE)
    comp_loc = models.ForeignKey(Loc, on_delete=models.CASCADE)
    comp_ean = models.CharField(max_length=60)
    comp_nserial = models.CharField(max_length=60)
    comp_addobs = models.TextField()
    comp_status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    comp_estado = models.CharField(max_length=30, choices=ESTADO_CHOICES)

    def __str__(self):
        return self.comp_name