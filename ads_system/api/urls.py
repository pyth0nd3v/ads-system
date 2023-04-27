from django.urls import path,include
from .views import AdsFilterView
from rest_framework.routers import DefaultRouter
from ads_system.api import views


# Initializing a Default router 
router = DefaultRouter()
router.register(r'ads', views.AdsViewSet,basename="ads")

urlpatterns = [
    path('', include(router.urls)),
    path('ad-filter/', AdsFilterView.as_view()),

]