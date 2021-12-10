from django.urls import path
from .views import SocialsSerializer

urlpatterns = {
    path('', SocialsSerializer.as_view()),
}