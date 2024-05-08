# from django.urls import path
# from users.views import PassportAPIView

# urlpatterns = [
#     path('users/', PassportAPIView.as_view(), name='user-list-create'),
#     path('users/<int:pk>/', PassportAPIView.as_view(), name='user-retrieve-update-destroy'),
# ]


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import PassportAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', PassportAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', PassportAPIView.as_view(), name='user-retrieve-update-destroy'),
]
