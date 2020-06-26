from django.urls import path, re_path
from . import views
app_name='deploy'
urlpatterns = [
    path('/',views.display,name='display'),
]
