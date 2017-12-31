from rest_framework import serializers
from mahasiswa.models import Mahasiswa

# class SerialisasiMahasiswa(serializers.Serializer):
#     nim = serializers.CharField(required=True, allow_blank=False, max_length=10)
#     nama = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     alamat = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     no_telp = serializers.CharField(required=False, allow_blank=True, max_length=13)
#     stat = serializers.CharField(required=True, allow_blank=False, max_length=2)
#     gender = serializers.CharField(required=True, allow_blank=False, max_length=1)
#     email = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     agama = serializers.CharField(required=True, allow_blank=False, max_length=20)
#     dob = serializers.CharField(required=True, allow_blank=False, max_length=10)
#     pwd = serializers.CharField(required=True, allow_blank=False, max_length=12)
#     en_pwd = serializers.CharField(max_length=255)
#
#     def create(self, validated_data):
#         return Mahasiswa.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.nim = validated_data.get('nim', instance.nim)
#         instance.nama = validated_data.get('nama', instance.nama)
#         instance.alamat = validated_data.get('alamat', instance.alamat)
#         instance.no_telp = validated_data.get('no_telp', instance.no_telp)
#         instance.stat = validated_data.get('stat', instance.stat)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.email = validated_data.get('email', instance.email)
#         instance.agama = validated_data.get('agama', instance.agama)
#         instance.dob = validated_data.get('dob', instance.dob)
#         instance.pwd = validated_data.get('pwd', instance.pwd)
#         instance.en_pwd = validated_data.get('en_pwd', instance.en_pwd)

class SeriMahasiswa(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ('nim', 'nama', 'alamat', 'no_telp', 'stat', 'gender', 'email', 'agama', 'dob', 'pwd', 'en_pwd')
