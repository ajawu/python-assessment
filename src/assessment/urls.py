from django.urls import path
from src.assessment import views

app_name = "assessment"

urlpatterns = [
    path('howold', views.AgeView.as_view(), name='age')
]
