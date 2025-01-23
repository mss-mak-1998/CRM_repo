from django.urls import path

from .views import home, login_user, logout_user, register_user, create_record, lead_record,lead_record_delete, lead_record_edit

app_name = 'website'

urlpatterns = [
    #BACKEND URL PATHS
    path('home/', home, name = 'home'),
    path('create/', create_record, name = 'create_record'),
    path('lead_record/<int:pk>/', lead_record, name = 'lead_record'),
    path('lead_record_delete/<int:pk>/', lead_record_delete, name = 'lead_record_delete'),
    path('lead_record_edit/<int:pk>/', lead_record_edit, name = 'lead_record_edit'),
    
    #AUTHENTICATION URLS
    path('', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', register_user, name = 'register'),
]
