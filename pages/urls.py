from django.urls import path
from .views import HomepageView, AboutPageView

urlpatterns = [
    path('', AboutPageView.as_view(), name= 'about'),
    path('', HomepageView.as_view(), name= 'home'),
    
]