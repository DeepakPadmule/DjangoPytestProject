# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Grievances, GrievanceTypes, GrievanceDetails
from .serializers import GrievancesSerializer, GrievanceTypesSerializer, GrievanceDetailsSerializer


class GrievanceList(APIView):
    # List all users, or create a new grievance.
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        grievance = Grievances.objects.all()
        serializer = GrievancesSerializer(grievance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GrievancesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------
class GrievanceUpdate(APIView):
    # Retrieve, update or delete a grievance instance.
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Grievances.objects.get(pk=pk)
        except Grievances.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grievance = self.get_object(pk)
        serializer = GrievancesSerializer(grievance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        grievance = self.get_object(pk)
        serializer = GrievancesSerializer(grievance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grievance = self.get_object(pk)
        grievance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------------------------
class GrievanceTypeList(APIView):
    # List all users, or create a new grievanceType.
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        grvType = GrievanceTypes.objects.all()
        serializer = GrievanceTypesSerializer(grvType, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GrievanceTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------
class GrievanceTypeUpdate(APIView):
    # Retrieve, update or delete a grievanceType instance.
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return GrievanceTypes.objects.get(pk=pk)
        except GrievanceTypes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grvType = self.get_object(pk)
        serializer = GrievanceTypesSerializer(grvType)
        return Response(serializer.data)


# -------------------------------------------------------
class GrievanceDetailList(APIView):
    # List all users, or create a new grievanceStatus.
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        grvStatus = GrievanceDetails.objects.all()
        serializer = GrievanceDetailsSerializer(grvStatus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GrievanceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------
class GrievanceDetailUpdate(APIView):
    # Retrieve, update or delete a grievanceStatus instance.
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return GrievanceDetails.objects.get(pk=pk)
        except GrievanceDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        grvStatus = self.get_object(pk)
        serializer = GrievanceDetailsSerializer(grvStatus)
        return Response(serializer.data)
