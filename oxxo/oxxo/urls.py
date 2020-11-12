"""oxxo URL Configuration"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from products.views import BeerViewSet
from products.views import BeerView
from products.views import UserView
from products.views import CustomerView
from products.views import OrderView

# Instacia de router para Viewsets
router = DefaultRouter()
router.register("products", BeerViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path("api/beers", BeerView.as_view()),
    path("api/customer", CustomerView.as_view()),
    path("api/orders", OrderView.as_view()),
    path("api/signup", UserView.as_view()),
    path('api/login', obtain_jwt_token, name='token_obtain_pair'),
]
