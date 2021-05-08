from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getpersonapi/', views.ListPersonApi.as_view()),
    path('postpersonapi/', views.CreatePersonApi.as_view()),
    path('getpersonapi/<int:pk>/', views.RetrieveAPIView.as_view()),
    path('putpersonapi/<int:pk>/', views.UpdatePersonApi.as_view()),
    path('deletepersonapi/<int:pk>/', views.DeletePersonApi.as_view()),
    path('personapi2/', views.ListCreatePersonApi.as_view()),
    path('personapi2/<int:pk>/', views.RetrieveUpdatePersonApi.as_view()),
    path('personapi3/<int:pk>/', views.RetrieveDeletePersonApi.as_view()),
    path('personapi4/<int:pk>/', views.RetrieveUpdateDeletePersonApi.as_view()),

]
