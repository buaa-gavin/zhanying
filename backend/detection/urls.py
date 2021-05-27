from django.urls import path

from . import views


app_name = 'detection'

urlpatterns = [
    path('InfoList/', views.InfoList.as_view(), name='index'),
    path('InfoList/<int:pk>/', views.InfoDetail.as_view(), name='detail'),

    # path('upload_file/', views.upload_file, name='upload_file'),
]

