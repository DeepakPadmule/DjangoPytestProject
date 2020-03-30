# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


def create_grievance_type_id():
    last_row = GrievanceTypes.objects.all().order_by('griev_type_id').last()
    
    if not last_row:
        return 'GT-' + "{0:04}".format(1)

    old_id = last_row.griev_type_id
    new_id = 'GT-' + "{0:04}".format(int(old_id[3:]) + 1)
    return new_id


def create_grievance_id():
    last_row = Grievances.objects.all().order_by('griev_id').last()

    if not last_row:
        return 'G-' + "{0:04}".format(1)

    old_id = last_row.griev_id
    new_id = 'G-' + "{0:04}".format(int(old_id[2:]) + 1)
    return new_id


def create_grievance_detail_id():
    last_row = GrievanceDetails.objects.all().order_by('griev_detail_id').last()

    if not last_row:
        return 'GD-' + "{0:04}".format(1)

    old_id = last_row.griev_detail_id
    # print(old_id)
    new_id = 'GD-' + "{0:04}".format(int(old_id[3:]) + 1)
    return new_id


# Create your models here.

class GrievanceTypes(models.Model):
    griev_type_id = models.CharField(max_length=10, primary_key=True, default=create_grievance_type_id, editable=False)
    # griev_type_id = models.CharField(max_length=10, primary_key=True)
    griev_type = models.CharField(max_length=45)

    @property
    def get_type(self):
        return self.griev_type


class Grievances(models.Model):
    griev_id = models.CharField(max_length=10, primary_key=True, default=create_grievance_id, editable=False)
    griev_type_id = models.ForeignKey(GrievanceTypes, on_delete=models.CASCADE, null=True)
    griev_title = models.CharField(max_length=45)
    griev_desc = models.CharField(max_length=255)
    griev_filed_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_title(self):
        return self.griev_title


class GrievanceDetails(models.Model):
    griev_detail_id = models.CharField(max_length=10, primary_key=True, default=create_grievance_detail_id,
                                       editable=False)
    griev_id = models.ForeignKey(Grievances, on_delete=models.CASCADE, null=True)
    griev_status = models.CharField(max_length=45, null=True)
    griev_status_desc = models.CharField(max_length=255, null=True)
    griev_st_desc_up_date = models.DateTimeField(auto_now=True)

    @property
    def get_status(self):
        return self.griev_status
