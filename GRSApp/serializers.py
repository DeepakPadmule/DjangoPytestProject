from rest_framework import serializers

from .models import Grievances, GrievanceDetails, GrievanceTypes


class GrievancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievances
        fields = '__all__'


class GrievanceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrievanceDetails
        fields = '__all__'


class GrievanceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrievanceTypes
        fields = '__all__'
