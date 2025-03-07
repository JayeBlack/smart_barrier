# apps/officer_auth/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Officer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = serializers.CharField()
        self.fields['password'] = serializers.CharField(write_only=True)
        # Remove any inherited email requirement

    def validate(self, attrs):
        username_input = attrs.get('username')
        password = attrs.get('password')

        # Check only the username field
        user = Officer.objects.filter(username=username_input).first()

        if user and user.check_password(password):
            self.user = user
        else:
            raise serializers.ValidationError(
                {"detail": "No active account found with the given credentials"}
            )

        refresh = self.get_token(self.user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ['id', 'badge_number', 'name', 'email', 'username', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'email': {'required': True},  # Email required for creation
        }

    def create(self, validated_data):
        officer = Officer.objects.create_user(
            email=validated_data['email'],
            badge_number=validated_data['badge_number'],
            name=validated_data['name'],
            username=validated_data.get('username'),
            password=validated_data['password'],
        )
        officer.role = validated_data.get('role', 'officer')
        officer.save()
        return officer

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.role = validated_data.get('role', instance.role)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance