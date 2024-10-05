from django.urls import path
from .views import docs_maker

urlpatterns = [
    path('', docs_maker, name='docs_maker'),
]