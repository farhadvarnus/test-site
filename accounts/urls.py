from django.urls import path
from django.contrib import admin
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", login_accounts, name='login_accounts'),
    path("signup/", signup_accounts, name='signup_accounts'),
    path("logout/", logout_accounts, name='logout_accounts'),
    path('', views.index, name='main.html'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html'), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),


]
