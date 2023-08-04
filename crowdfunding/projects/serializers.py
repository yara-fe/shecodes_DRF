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

    #Update a project - can be partial information
    #Looks into what's already in the database andd determines which fields to update
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance    