from django.urls import path
from . import views

app_name = 'academics'
urlpatterns = [
    path('', views.ProgramListView.as_view(), name='program_list'),
    path('<slug:slug>/', views.ProgramDetailView.as_view(), name='program_detail'),
]