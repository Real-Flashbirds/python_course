from django.urls import path, include

from . import views

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'banks', views.BankViewSet)
router.register(r'branches', views.BranchViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'accounts', views.AccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]