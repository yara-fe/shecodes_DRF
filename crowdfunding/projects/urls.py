from rest_framework.urlpatterns import format_suffix_patterns #formats url 
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) 