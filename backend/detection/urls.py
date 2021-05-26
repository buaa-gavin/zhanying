from django.urls import path
from . import views

app_name = 'detection'

urlpatterns = [
    path('InfoList/', views.info_list, name='index'),
    # path('InfoList/<int:id>/', views.detail, name='detail'),
    # path('upload_file/', views.upload_file, name='upload_file'),
]
