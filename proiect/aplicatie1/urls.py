from django.urls import path
from aplicatie1 import views

app_name = 'aplicatie1'

urlpatterns = [
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateLocationView.as_view(), name='modificare'),
    path('<int:pk>/dezactiveaza/', views.deactivate_location, name='dezactivare'),
    path('<int:pk>/activeaza/', views.activate_location, name='activare')
]
