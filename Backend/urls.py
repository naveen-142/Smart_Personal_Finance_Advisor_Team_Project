from django.urls import path
from .views import contact_message, predict, home
from . import views
urlpatterns = [
    path('', home, name='home'),  
    path('predict/', views.predict, name='predict'),  
    path('history/', views.get_history, name='history'),
    path('contact/', contact_message, name='contact_message'),
]

