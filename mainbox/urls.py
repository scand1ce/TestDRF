from django.urls import path, include
from .views import apiOverview, DiscrViewSet, ItemViewSet, BoxViewSet
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

swagger_view = get_swagger_view(title='SWAGGER API')

router = DefaultRouter()
router.register(r'descriptions', DiscrViewSet, basename='descriptions')
router.register(r'items', ItemViewSet, basename='items')
router.register(r'boxes', BoxViewSet, basename='boxes')
# router.register(r'boxes/<int:pk>', BoxDetail, basename='box')


urlpatterns = [
    path('', apiOverview),
    path(r'', include(router.urls)),
#     path('boxes/', BoxView.as_view()),
#     path('boxes/<int:pk>/', BoxDetail.as_view()),
    path('swagger/', swagger_view),
]
