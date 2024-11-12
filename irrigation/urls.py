from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('control/', views.irrigation_control, name='irrigation_control'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control/', views.irrigation_control, name='irrigation_control'),
    path('history/', views.irrigation_history, name='irrigation_history'),
    path('dashboard/' , views.dashboard, name='dashboard'),
     
    
]