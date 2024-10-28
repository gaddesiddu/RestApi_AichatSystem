from django.urls import path
from .views import RegisterUser, LoginUser, ChatView, TokenBalanceView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register_user"),
    path('login/', LoginUser.as_view(), name="login_user"),
    path('chat/', ChatView.as_view(), name="chat"),
    path('balance/', TokenBalanceView.as_view(), name="balance_of_tokens"),
]
