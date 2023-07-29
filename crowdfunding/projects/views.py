from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(APIView):

    #defines GET request
    def get(self, request):
        projects = Project.objects.all() #gets all data from DB
        serializer = ProjectSerializer(projects, many=True) #converts projects into json
        return Response(serializer.data) #sends response as a json