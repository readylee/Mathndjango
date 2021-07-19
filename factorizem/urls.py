from django.urls import path

from . import views

app_name = 'factorizem'
urlpatterns = [
    path('', views.FactorizemView.as_view(), name='index'),
    # path('', views.index, name='index'),
]