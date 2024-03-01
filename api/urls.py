from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreate.as_view(), name='course-view-create'),
    path('courses/<int:pk>', views.CourseRetriveUpdateDestroy.as_view(), name='update')
]
