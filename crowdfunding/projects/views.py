from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.http import Http404
from rest_framework import status

class ProjectList(APIView):

    #defines GET request
    def get(self, request):
        projects = Project.objects.all() #gets all data from DB
        serializer = ProjectSerializer(projects, many=True) #converts projects into json
        return Response(serializer.data) #sends response as a json
    
    #defines POST request - creating a project
    def post(self, request):
        serializer = ProjectSerializer(data=request.data) #loads request data into serializer
        if serializer.is_valid():
            serializer.save() #save a new record to DB
            # return Response(serializer.data) #respond with JSON with save details
            return Response(    
                serializer.data,
                status=status.HTTP_201_CREATED #success status if created
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST  #error handling
        )


class ProjectDetail(APIView):

    #returns object from the DB that has matching PK in the request
    def get_object(self, pk):
            # return Project.objects.get(pk=pk)
            try:
                return Project.Objects.get(pk=pk)  #return ID if available
            except Project.DoesNotExist:
                 raise Http404  #error handling if attempt fails

    #defines GET request for a particular record/ Primary Key
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

