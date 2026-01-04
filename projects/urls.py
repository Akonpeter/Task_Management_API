from django.urls import path
from .views import ProjectsListCreateView, ProjectsDetailView

urlpatterns = [
    path('', ProjectsListCreateView.as_view(), name='projects-list'),
    path('<int:pk>/', ProjectsDetailView.as_view(), name='projects-detail'),
    
]
