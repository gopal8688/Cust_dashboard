from django.db import models


class Method(models.Model):
    name = models.CharField(max_length=50, unique=True)
    descripton = models.TextField(null=False)


class Instrument(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    asset_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    checksum_string = models.CharField(max_length=128, null=True)
    FK_instr_type = models.ForeignKey(InstrType, related_name='installations', on_delete=models.PROTECT)
    Instr_Version = models.ManyToManyField(Version,through='Instr_Version', related_name='Instr_Version')
