from django.db import models
from django.core.exceptions import ValidationError


def validate_not_spaces(nilai):
    if isinstance(nilai, str) and nilai.strip() == '':
        raise ValidationError(u"Just Space is not Allowed")


class Mahasiswa(models.Model):
    nim = models.CharField(max_length=10, blank=False, primary_key=True, validators=[validate_not_spaces])
    nama = models.CharField(max_length=100, blank=False, validators=[validate_not_spaces])
    alamat = models.CharField(max_length=100, blank=False, validators=[validate_not_spaces])
    no_telp = models.CharField(max_length=13, blank=True, default='')
    stat = models.CharField(max_length=2, blank=False, validators=[validate_not_spaces])
    gender = models.CharField(max_length=1, blank=False, validators=[validate_not_spaces])
    email = models.CharField(max_length=100, blank=True, default='')
    agama = models.CharField(max_length=20, blank=False, validators=[validate_not_spaces])
    dob = models.CharField(max_length=10, blank=False, validators=[validate_not_spaces])
    pwd = models.CharField(max_length=12, blank=False, validators=[validate_not_spaces])
    en_pwd = models.CharField(max_length=255)
