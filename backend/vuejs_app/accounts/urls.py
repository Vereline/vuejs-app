from django.conf.urls import url, include
from accounts.views import LogoutView, SignUpView, UpdateUserView
from accounts.serializers import EmailAndUsernameJWTSerializer
from rest_framework_jwt.views import ObtainJSONWebToken, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^token-auth/', ObtainJSONWebToken.as_view(serializer_class=EmailAndUsernameJWTSerializer),
        name='obtain_token'),  # login view
    url(r'^token-refresh/', refresh_jwt_token, name='refresh_token'),
    url(r'^token-verify/', verify_jwt_token, name='verify_token'),
    # apply 2 migrations to use this thing
    url(r'^password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^signup/', SignUpView.as_view(), name='signup'),
    url(r'^update/', UpdateUserView.as_view({'post': 'post'}), name='update'),
    url(r'^user-profile/(?P<pk>\d+)/$', UpdateUserView.as_view({'get': 'user_profile'}), name='user_profile'),
    url(r'^profile/', UpdateUserView.as_view({'get': 'profile'}), name='profile'),
]
