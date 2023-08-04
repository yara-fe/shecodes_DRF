# Converts model to json format
from rest_framework import serializers
from django.apps import apps

#depicts Pledges as JSON
class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source="supporter.id")
    #gets all the data from the model
    class Meta:
        model = apps.get_model('projects.Pledge') #define model to convert
        fields ='__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    #get all the information about the pledges associated with project
    # pledges = PledgeSerializer(many=True, read_only=True)
    #gets all the data from the model
    class Meta:
        model = apps.get_model('projects.Project') #define model to convert
        fields ='__all__'


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)