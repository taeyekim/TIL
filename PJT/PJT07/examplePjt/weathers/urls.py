from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('save-data/', views.save_data, name="save_data"),
    path('list-data/', views.list_data, name="list_data"),
    path('hot-weathers/', views.hot_weathers, name="hot_weathers")
]