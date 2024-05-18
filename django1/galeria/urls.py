from django.urls import path
from galeria.views import index1

urlpatterns = [
    path('', index1),
]