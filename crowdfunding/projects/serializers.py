# Converts model to json format
from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):

    #gets all the data from the model
    class Meta:
        model = apps.get_model('projects.Pledge') #define model to convert
        fields ='__all__'


class ProjectSerializer(serializers.ModelSerializer):

    #gets all the data from the model
    class Meta:
        model = apps.get_model('projects.Project') #define model to convert
        fields ='__all__'