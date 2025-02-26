from django.urls import path
from .views import get_all_users, get_user_by_email, delete_user  

urlpatterns = [  # Define urlpatterns first
    path('users/', get_all_users, name='all_users'),
    path('user/<str:email>/', get_user_by_email, name='user_by_email'),
    path('delete-user/<str:email>/', delete_user, name='delete_user'),
]
