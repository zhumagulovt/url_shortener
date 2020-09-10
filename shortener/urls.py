from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', TemplateView.as_view(template_name="shortener/index.html")),
    path('add/', views.add, name='add'),
    path('link/<int:pk>', views.LinkDetailView.as_view(), name='link-detail'),
    path('links/', views.links_list),
    path('<str:url>/', views.short_url),
]