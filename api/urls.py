from django.urls import path
from .views import *


urlpatterns = [
    path("records", Records.as_view(), name="record"),
    path("country", Countries.as_view(), name="country"),
    path("sector", Sectors.as_view(), name="sector"),
]