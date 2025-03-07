# apps/checkpoints/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CheckpointLog
from .serializers import CheckpointLogSerializer
from apps.officer_auth.permissions import IsAdminRole
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CheckpointLogCreateView(generics.CreateAPIView):
    queryset = CheckpointLog.objects.all()
    serializer_class = CheckpointLogSerializer
    permission_classes = [IsAuthenticated]  # Any officer can log

class CheckpointLogRetrieveView(generics.RetrieveAPIView):
    queryset = CheckpointLog.objects.all()
    serializer_class = CheckpointLogSerializer
    permission_classes = [IsAuthenticated]  # Any officer can view
    lookup_field = 'id'

class CheckpointLogUpdateView(generics.UpdateAPIView):
    queryset = CheckpointLog.objects.all()
    serializer_class = CheckpointLogSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Admin-only
    lookup_field = 'id'

class CheckpointLogDeleteView(generics.DestroyAPIView):
    queryset = CheckpointLog.objects.all()
    serializer_class = CheckpointLogSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Admin-only
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': 'success',
            'message': 'Checkpoint log deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)