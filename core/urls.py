from django.urls import path, include
from .views import BootstrapFilterView

app_name = 'core'

urlpatterns = [
    path('', BootstrapFilterView, name='bootstrap'),

]
