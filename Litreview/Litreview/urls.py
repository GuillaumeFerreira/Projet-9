"""Litreview URL Configuration

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
import ticket.views
import profiles.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", profiles.views.LoginPageView.as_view(), name="login"),
    path("logout/", profiles.views.LogoutPageView.as_view(), name="logout"),
    path("home/", profiles.views.HomeView.as_view(), name="home"),
    path("signup/", profiles.views.SignupPage.as_view(), name="signup"),
    path(
        "create_ticket/", ticket.views.CreateTicketViews.as_view(), name="create_ticket"
    ),
    path(
        "create_ticket_review/",
        ticket.views.CreateTicketReviewViews.as_view(),
        name="create_ticket_review",
    ),
    path("subscription/", profiles.views.Followers.as_view(), name="subscription"),
    path(
        "delete_follower/<slug:pk>/",
        profiles.views.FollowerDeleteView.as_view(),
        name="delete_follower",
    ),
    path(
        "update_ticket/<int:pk>/",
        ticket.views.UpdateTicketViews.as_view(),
        name="update_ticket",
    ),
    path(
        "update_review/<int:pk>/",
        ticket.views.UpdateReviewViews.as_view(),
        name="update_review",
    ),
    path(
        "delete_ticket/<int:pk>/",
        ticket.views.TicketDeleteView.as_view(),
        name="delete_ticket",
    ),
    path(
        "delete_review/<int:pk>/",
        ticket.views.ReviewDeleteView.as_view(),
        name="delete_review",
    ),
    path("posts/", profiles.views.MyPostsView.as_view(), name="posts"),
    path(
        "create_review_from_ticket/<int:ticket_id>/",
        ticket.views.CreateReviewFromTicketViews.as_view(),
        name="create_review_from_ticket",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
