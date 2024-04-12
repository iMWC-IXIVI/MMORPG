from django.urls import path

from .views import (MainView, SignInView, accept_mail, accept_in_mail,
                    logout_user, add_subscribe, UserProfile, UserProfileUpdate)


urlpatterns = [
    path('', MainView.as_view(), name='register'),  # Главная страница форума
    path('sign-in/', SignInView.as_view(), name='sign_in'),  # Страница авторизации на форуме
    path('accept/<str:token>/', accept_mail, name='accept_mail'),  # Подтверждение регистрации пользователя
    path('accept-in/<str:token>/', accept_in_mail, name='accept_in_mail'),  # Подтверждение авторизации
    path('logout/', logout_user, name='logout'),  # Выход из профиля
    path('subscribe/', add_subscribe, name='add_subscribe'),  # Подписка на недельную рассылку
    path('my-profile/', UserProfile.as_view(), name='user_profile'),  # Профиль пользователя
    path('my-profile/update/<int:pk>/', UserProfileUpdate.as_view(), name='user_profile_update')  # Изменение профиля
]
