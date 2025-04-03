from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, ApplicationViewSet, ResourceViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]