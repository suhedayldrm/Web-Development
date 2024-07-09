# projects/models.py

from django.db import models
from django.urls import reverse
from django.db.models import QuerySet

import json


class ProjectManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(ProjectManager, self).get_queryset()


class Project(models.Model):
    project_title = models.CharField(max_length=755, null=True, blank=True)
    project_id = models.AutoField(primary_key=True)
    dfg_verfahren = models.CharField(max_length=455, null=True, blank=True)
    researchers = models.JSONField(null=True, blank=True, max_length=2000)
    institutions = models.JSONField(null=True, blank=True, max_length=2000)
    antragstellende_mitverantwortliche = models.JSONField(null=True, blank=True, max_length=2000)
    applicant = models.JSONField(null=True, blank=True)

    objects = ProjectManager()
    
    class Meta:
        db_table = "project"
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse("projects_detail", args=[str(self.project_id)])
    
    
class Person(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    person_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=400, null=True, blank=True)
    current_inst = models.CharField(max_length=600, null=True, blank=True)
    category = models.CharField(max_length=400, null=True, blank=True)
    projects = models.ManyToManyField(Project, related_name='people', blank=True)
    
    
    class Meta:
        db_table = "person"
        verbose_name_plural = 'people'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("people_detail", args=[str(self.person_id)])



    