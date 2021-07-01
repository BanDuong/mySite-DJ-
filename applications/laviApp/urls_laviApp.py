from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index',views.index,name="index"),
    path('list',views.getList.as_view(),name="list"),
    path('detail',views.getDetail.as_view(),name="detail"),
]