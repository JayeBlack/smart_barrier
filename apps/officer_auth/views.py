# apps/officer_auth/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from .models import Officer
from .serializers import OfficerSerializer, CustomTokenObtainPairSerializer
from .permissions import IsAdminRole
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'status': 'success',
            'data': serializer.validated_data,
            'message': 'Login successful'
        }, status=status.HTTP_200_OK)

class CustomTokenBlacklistView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'status': 'success',
            'message': 'Logout successful'
        }, status=status.HTTP_205_RESET_CONTENT)

@method_decorator(csrf_exempt, name='dispatch')
class OfficerCreateView(generics.CreateAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

class OfficerRetrieveView(generics.RetrieveAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class OfficerUpdateView(generics.UpdateAPIView):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

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