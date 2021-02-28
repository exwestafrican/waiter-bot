"""waiter_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path, include
from messaging import webhook
from rest_framework import routers
from users.views import *
from users.admin_api.views import *
from commands.views import *
from location.admin_api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

base_url = "api/v1/"

router = routers.DefaultRouter()
admin_router = routers.DefaultRouter()

router.register("users", UserModelViewSet, basename="users")
router.register("commands", CommandModelViewSet, basename="commands")

admin_router.register(
    "restaurants", RestaurantAdminModelViewSet, basename="restaurants"
)
admin_router.register("users", UserAdminModelViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path(base_url + "webhooks/message_received/", webhook.message_received),
    path(base_url + "webhooks/send_message/", webhook.send_message),
    path(base_url, include(router.urls)),
    path(base_url + "admin/", include(admin_router.urls)),
    path("api/v1/rest-auth/registration/", include("rest_auth.registration.urls")),
    path("api/v1/rest-auth/", include("rest_auth.urls")),
]
