from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'region', views.RegionViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'GDP', views.GDPViewSet)
router.register(r'FieldGDP', views.FieldGDPViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'testBar', views.TestView.as_view(), name='Test View'),
    path(r'testView', views.IndexView.as_view(), name='Test View'),
]