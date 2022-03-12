from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=80, allow_blank=False)
    first_name = serializers.CharField(max_length=80, allow_blank=False)
    last_name = serializers.CharField(max_length=80, allow_blank=False)
    email = serializers.EmailField(max_length=80, allow_blank=False)
    password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'password']

    def validate(self, attrs):
        email = User.objects.filter(email=attrs.get('email')).exists()
        username = User.objects.filter(username=attrs.get('username')).exists()

        if email:
            raise ValidationError(
                detail="User with email exists", code=status.HTTP_403_FORBIDDEN)

        if username:
            raise ValidationError(
                detail="User with username exists", code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)

    def create(self, validated_data):
        new_user = User(**validated_data)

        new_user.password = make_password(validated_data.get('password'))

        new_user.save()

        return new_user


class UserLoginSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=255)
    last_name = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    roles = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'username': user.username,
                'email': user.email

            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email',
                  'last_name', 'first_name', 'password']
        extra_kwargs = {"password": {"write_only": True}}
