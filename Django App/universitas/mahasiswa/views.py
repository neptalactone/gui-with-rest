from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mahasiswa.models import Mahasiswa
from mahasiswa.serializers import SeriMahasiswa


@api_view(['GET','POST'])
def list_mahasiswa(request, format=None):
    if request.method == 'GET':
        mahasiswa = Mahasiswa.objects.all()
        seri = SeriMahasiswa(mahasiswa, many=True)
        return Response(seri.data)

    elif request.method == 'POST':
        seri = SeriMahasiswa(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def detail_mahasiswa(request, nim, format=None):
    try:
        mahasiswa = Mahasiswa.objects.get(nim=nim)
    except Mahasiswa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        seri = SeriMahasiswa(mahasiswa)
        return Response(seri.data)

    elif request.method == 'PUT':
        seri = SeriMahasiswa(mahasiswa, data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mahasiswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
