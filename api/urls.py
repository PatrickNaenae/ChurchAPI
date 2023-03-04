from django.urls import path
from .views import get_members, create_member, check_email_exists, check_phone_exists
urlpatterns = [
    path('', get_members, name='members-list'),
    path('create-member/', create_member, name='create-member'),
    path('check_if_exists/email/<str:email>/', check_email_exists, name='check-email-exists'),
    path('check_if_exists/phone/<str:phone>/', check_phone_exists, name='check-phone-exists'),
]