"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='app/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('flux/', views.flux),
    path('subscriptions/', views.subscriptions),
    path('create_ticket/', views.create_ticket),
    path('create_review/', views.create_review),
    path('post/', views.post),
    path('to_modify_review/', views.to_modify_review),
    path('to_modify_ticket/', views.to_modify_ticket),

]
