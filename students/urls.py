from django.urls import path
from . import views
from .views import StudentCreate

urlpatterns = [
 path('list/', views.list_view,name='list'),
 path('create/', StudentCreate.as_view() ),
 path('home/',views.home_view,name='home'),
 path('home2/',views.home_view2,name='home2'),

    
]