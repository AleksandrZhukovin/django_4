from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_create/', views.project_create, name='project_create'),
    path('project/<int:id>', views.project, name='project')
]
