from django.urls import path
from .views import UserList, UserDetail
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]