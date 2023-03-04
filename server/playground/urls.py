from django.urls import path
from . import views

urlpatterns = [
    path('addQuestion/', views.addQuestion),
    path('getQuestions/', views.getAllQuestions),
        path('deleteQuestion/', views.deleteQuestion),


]