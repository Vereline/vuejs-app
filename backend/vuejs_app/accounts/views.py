import logging
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import update_last_login
from django.contrib.auth import logout
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings

from accounts.utils import validate_date
from accounts.serializers import UserSerializer, UserProfileSerializer
from accounts.models import User

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

logger = logging.getLogger(__name__)


# Create your views here.

# TODO: please, don't use this code again in the future(some parts were borrowed from your previous projects),
#  write your own code, which will be more qualitative

# TODO: I mean these views, serializers and that ugly code in the models.py file

class SignUpView(APIView):
    """
    API endpoint to sign up
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        user_data = request.data
        existing_users_username = User.objects.filter(username=request.data['username'])
        existing_users_email = User.objects.filter(email=request.data['email'])

        if existing_users_username or existing_users_email:
            return Response({'error': 'User with specified email or username already exists'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            if 'birth_date' in user_data:
                validate_date(user_data['birth_date'])
        except Exception as ex:
            logger.error(ex.__str__())
            return Response({'error': ex.__str__()}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user_data['password'])
        user.is_active = True
        user.save()
        update_last_login(None, user)

        # return token after user creation
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token}, status=status.HTTP_201_CREATED)


class UpdateUserView(ModelViewSet):
    """
    API endpoint to update user data
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    parser_classes = (JSONParser, MultiPartParser,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        user_data = request.data
        serializer = self.get_serializer(request.user, data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if 'password' in user_data:
            user.set_password(user_data['password'])
            user.save()

        # return token after user update
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token}, status=status.HTTP_201_CREATED)

    def profile(self, request):
        """
        Get info about current user
        """
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def user_profile(self, request, pk):
        """
        Get info about user
        """
        user = self.get_object()
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
    API endpoint to logout
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({'user': 'Success logout'}, status=status.HTTP_204_NO_CONTENT)
