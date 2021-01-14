from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("password_reset", views.password_reset_request, name="password_reset"),
]