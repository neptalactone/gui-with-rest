from mahasiswa.models import Mahasiswa
from mahasiswa.serializers import SeriMahasiswa
from rest_framework.renderers import JSONRenderer
import base64
from django.conf import settings


settings.configure(settings)


nim = input("Masukkan NIM : ")
nama = input("Masukkan Nama : ")
alamat = input("Masukkan alamat : ")
no_telp = input("Masukkan No.telp : ")
stat = input("Masukkan status : ")
gender = input("Masukkan gender : ")
email = input("Masukkan email : ")
agama = input("Masukkan agama : ")
dob = input("Masukkan tanggal lahir : ")
pwd = input("Masukkan password : ")
en_pwd = base64.b64encode(pwd.encode('utf-8'))

mahasiswa = Mahasiswa(nim=nim, nama=nama, alamat=alamat, no_telp=no_telp, stat=stat, gender=gender, email=email,
                      agama=agama, dob=dob, pwd=pwd, en_pwd=en_pwd)

mahasiswa.save()

seriMahasiswa = SerialisasiMahasiswa(mahasiswa)
print(seriMahasiswa.data)

kontenMahasiswa = JSONRenderer().render(seriMahasiswa)
print(seriMahasiswa.data)
