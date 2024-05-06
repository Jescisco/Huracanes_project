from django.urls import path, include
from rest_framework import routers
from login import views

router = routers.DefaultRouter()
router.register(r'login', views.LoginView, 'login')

#Here im generating the queries get, post, put and delete

urlpatterns = [
    path("api/", include(router.urls))
]