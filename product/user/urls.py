from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
]