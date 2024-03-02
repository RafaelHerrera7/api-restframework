from django.shortcuts import render
from rest_framework import generics
from .models import Course, Topic, Teacher
from .serializers import CourseSerializer, TopicSerializer, TeacherSerializer

# Create your views here.
#COURSE
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'

#TOPIC
class TopicListCreate(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

#TEACHER 
class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer