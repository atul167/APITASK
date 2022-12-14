from django.urls import path
from .views import *

urlpatterns = [
    path('',SignUpAPIView.as_view()),
    path('signup', SignUpAPIView.as_view()),
    path('otp',OtpView.as_view()),
    path('personalinfo/',PersonalInfoView.as_view())
]