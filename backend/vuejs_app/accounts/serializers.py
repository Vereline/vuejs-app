from accounts.models import User
from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'date_joined',
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'first_name',
            'last_name',
            'birth_date',
            'photo',
        )
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'date_joined',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'first_name',
            'last_name',
            'birth_date',
            'photo',
        )


class EmailAndUsernameJWTSerializer(JSONWebTokenSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):
        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("username_or_email")).first() or User.objects.filter(
            username=attrs.get("username_or_email")).first()
        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = 'User account is disabled.'
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)
                    update_last_login(None, user)
                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = 'Unable to log in with provided credentials.'
                    raise serializers.ValidationError(msg)

            else:
                msg = 'Must include "{username_field}" and "password".'
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = 'Account with this email/username does not exists'
            raise serializers.ValidationError(msg)
