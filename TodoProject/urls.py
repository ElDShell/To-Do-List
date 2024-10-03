"""
URL configuration for TodoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
# from library import views
from TodoApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',include('TodoApp.urls'),name='todo'),
    path('', RedirectView.as_view(url='todo/home')),
    path('accounts/',include('django.contrib.auth.urls'),),
    path('accounts/register',views.Register.as_view(),name='register'),
    path('accounts/password-change/', views.ChangePassword.as_view(), name='password-change'),
    path('accounts/password-change/done/',views.ChangePasswordDone.as_view(),name='password_change_done',),
    path("accounts/password-reset/", views.ResetPassword.as_view(), name="password-reset"),
    path('accounts/password-reset/done/',views.ResetPasswordDone.as_view(),name='password_reset_done',),
    path("accounts/password-reset/<uidb64>/<token>/", views.ResetPasswordConfirm.as_view(), name="password-reset-confirm"),
    path('accounts/reset/complete/',views.ResetDone.as_view(),name='reset-one',),
]

