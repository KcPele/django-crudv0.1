
from django.urls import path
from .views import Home

urlpatterns = [
    path('', Home.as_view(template_name='home.html'), name='home')

]