from rest_framework import routers
from django.conf.urls import url, include
from . import views
from .views import PostViewSet

urlpatterns = [
    url(r'^$' ,views.index, name='index'),
    ]

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
