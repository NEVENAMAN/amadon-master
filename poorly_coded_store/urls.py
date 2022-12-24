from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('Report_buy',views.Report_buy),
    path('test',views.test),
]
