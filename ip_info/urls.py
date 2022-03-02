from django.contrib import admin
from django.urls import path

from csv_app.views import download_csv

urlpatterns = [
    path('export-csv/', download_csv, name='export_csv'),
    path('admin/', admin.site.urls),
]
