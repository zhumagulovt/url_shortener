from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginView),
    path('registration/', views.registration),
    path('logout/', views.logout_view)
]