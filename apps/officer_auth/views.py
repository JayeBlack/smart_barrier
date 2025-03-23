# apps/officer_auth/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from .models import Officer
from .serializers import OfficerSerializer, CustomTokenObtainPairSerializer
from .permissions import IsAdminRole, IsSelfOrAdmin


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'status': 'success',
            'data': serializer.validated_data['data'],  # Extract 'data' from serializer
            'message': 'Login successful'
        }, status=status.HTTP_200_OK)


class CustomTokenBlacklistView(TokenBlacklistView):
    permission_classes = [IsAuthenticated]  # Require authentication for logout

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Logout successful'
        }, status=status.HTTP_205_RESET_CONTENT)


class OfficerCreateView(generics.CreateAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'status': 'success',
            'data': serializer.data,
            'message': 'Officer created successfully'
        }, status=status.HTTP_201_CREATED)


class OfficerRetrieveView(generics.RetrieveAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated, IsSelfOrAdmin]
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class OfficerUpdateView(generics.UpdateAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated, IsSelfOrAdmin]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'status': 'success',
            'data': serializer.data,
            'message': 'Officer updated successfully'
        }, status=status.HTTP_200_OK)


class OfficerDeleteView(generics.DestroyAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': 'success',
            'message': 'Officer deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
