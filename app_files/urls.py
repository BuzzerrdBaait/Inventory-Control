from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

from django.urls import path

from .views import *

app_name = "app_files"

urlpatterns = [
     
    path('', views.home, name='home'),

    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]



