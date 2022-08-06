
from django.urls import path
from .views import Home, FileUploadDetailView

urlpatterns = [
    path('', Home.as_view(template_name='home.html'), name='home'),
    path('details/<int:pk>/', FileUploadDetailView.as_view(), name='details')

]