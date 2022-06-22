from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework_nested import routers
from API.views import SignupViewset, ClientViewset, ContractViewset, EventViewset


client_router = routers.SimpleRouter()
client_router.register(r"clients?", ClientViewset, basename="clients")

contract_router = routers.SimpleRouter()
contract_router.register(r"contracts?", ContractViewset, basename="contracts")

event_router = routers.SimpleRouter()
event_router.register(r"events?", EventViewset, basename="events")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/signup/', SignupViewset.as_view(), name='signup'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include(client_router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls))
]
