from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/', views.event_list_by_month, name='event_list_by_month'),
    path('', views.event_list_by_month, name='home'),
]
