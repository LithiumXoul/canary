from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('notices/',views.notices,name='notices'),
    path('results/',views.results,name='results'),
    path('routine/',views.routine,name='routine'),
    path('contact/',views.contact,name='contact'),
    path('admission/',views.admission,name='admission'),
    path('view_notice/<str:pk>',views.view_notice,name='view_notice'),
    path('view_result/<str:pk>',views.view_result,name='view_result')
]