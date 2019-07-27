
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from classesAPI.views import *

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    # path('list/', ClassroomListAPI.as_view(), name='list'),
    path('detail/<int:classroom_id>/', ClassroomDetailAPI.as_view(), name='detail'),
    path('create/', ClassroomCreateAPI.as_view(), name='create'),
    path('delete/<int:classroom_id>/', ClassroomDeleteAPI.as_view(), name='delete'),
    path('update/<int:class_id>/', ClassroomUpdateAPI.as_view(), name='update'),
    path('register/', Registration.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login')
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
