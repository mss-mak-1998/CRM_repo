from django.urls import path

from .views import home, login_user, logout_user, register_user, create_record, lead_record

app_name = 'website'

urlpatterns = [
    #BACKEND URL PATHS
    path('', home, name = 'home'),
    path('create/', create_record, name = 'create_record'),
    path('lead_record/<int:pk>/', lead_record, name = 'lead_record'),
    
    #AUTHENTICATION URLS
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', register_user, name = 'register'),
]
