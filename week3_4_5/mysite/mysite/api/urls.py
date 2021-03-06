from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from mysite.api import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('reg/', views.RegistrationView.as_view())
]