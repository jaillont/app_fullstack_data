from django.urls import path

import user.views


urlpatterns = [
    path(
        '',
        user.views.hello
    ),
    path(
        'login',
        user.views.login_page,
        name='login'
    ),
    path(
        'logout/',
        user.views.logout_user,
        name='logout'
    ),
    path(
        'signup/',
        user.views.signup_page,
        name='signup'
    ),
]