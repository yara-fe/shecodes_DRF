from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
    
    #Checks user permissions
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    #returns object from the DB that has matching PK in the request
    def get_object(self, pk):
            # return Project.objects.get(pk=pk)
            try:
                project = Project.Objects.get(pk=pk)  #return ID if available
                self.check_object_permissions(self.request, project)
                return project            
            except Project.DoesNotExist:
                raise Http404  #error handling if attempt fails

    #defines GET request for a particular record/ Primary Key
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    #defines PUT method - replaces a record within the database, but partial info can be ok
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()

class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )