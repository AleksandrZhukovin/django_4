from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('project_create/', views.project_create, name='project_create'),
    path('project/<int:id>', views.project, name='project'),
    path('pr_edit/<int:id>', views.project_edit, name='project_edit'),
    path('logout/', views.LogoutPage.as_view(), name='logout')
]
