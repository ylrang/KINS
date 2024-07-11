from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegulationSerializer, CaseSerializer
from .models import Regulation, Case

class RegulationList(APIView):
    def get(self, request):
        reg_list = Regulation.objects.all()
        serializer = RegulationSerializer(reg_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RegulationDetail(APIView):
    def get(self, request, pk):
        reg = get_object_or_404(Regulation, pk=pk)
        serializer = RegulationSerializer(reg)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            reg = Regulation.objects.get(pk=pk)
            reg.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class CaseList(APIView):
    def get(self, request):
        queryset = Case.objects.all()
        if request.query_params:
            org = request.query_params.get('organization', None)
            queryset = queryset.filter(organization=org)
        serializer = CaseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CaseDetail(APIView):
    def get(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            case = Case.objects.get(pk=pk)
            case.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)