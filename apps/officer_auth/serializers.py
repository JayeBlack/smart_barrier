# apps/officer_auth/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import Officer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)
        self.fields['email'] = serializers.EmailField(required=True)
        self.fields['password'] = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError(
                {"detail": "No active account found with the given credentials"}
            )

        self.user = user
        refresh = self.get_token(self.user)
        return {
            'status': 'success',
            'data': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['id', 'badge_number', 'name', 'email', 'password', 'role', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'email': {'required': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def validate_email(self, value):
        if self.instance is None and Officer.objects.filter(email=value).exists():
            raise serializers.ValidationError("An officer with this email already exists.")
        return value

    def validate_badge_number(self, value):
        if self.instance is None and Officer.objects.filter(badge_number=value).exists():
            raise serializers.ValidationError("An officer with this badge number already exists.")
        return value

    def create(self, validated_data):
        officer = Officer.objects.create_user(
            email=validated_data['email'],
            badge_number=validated_data['badge_number'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        officer.role = validated_data.get('role', 'officer')
        officer.save()
        return officer

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
