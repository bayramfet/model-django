from django.urls import path, include

from .views import fscohort, fscohort2

urlpatterns = [
    path('', fscohort),
    path('example/', fscohort2),
]