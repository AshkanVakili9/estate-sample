from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('create/', views.create_file_record, name='create_file_record'),
#     # path('edit/<int:pk>/', views.edit_file_record, name='edit_file_record'),
# ]
