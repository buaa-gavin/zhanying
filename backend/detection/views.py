# Create your views here.
from rest_framework.response import Response
from django.http import JsonResponse
from detection.models import Person,Diagnose
from detection.serializers import *
from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets


class InfoList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer


class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer


class DiagnoseDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseSerializer


class DiagnoseViewSet(viewsets.ModelViewSet):
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseSerializer


# @api_view(['PUT'])
# def upload(request):
#     data = request.data
#     personId =

#
# @api_view(['GET','POST'])
# def info_list(request):
#     if request.method == 'GET':
#         info = Person.objects.all()
#         serializer = PersonListSerializer(info, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PersonListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# def info_detail(request, id):
#     info = Person.objects.get(id=id)
#     diagnose_set = info.diagnose_set.all()
