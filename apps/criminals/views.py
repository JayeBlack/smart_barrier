# apps/criminals/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CriminalRecord
from .serializers import CriminalRecordSerializer
from apps.officer_auth.permissions import IsAdminRole
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class CriminalRecordCreateView(generics.CreateAPIView):
    queryset = CriminalRecord.objects.all()
    serializer_class = CriminalRecordSerializer
    permission_classes = [IsAuthenticated]  # Any officer can create


class CriminalRecordRetrieveView(generics.RetrieveAPIView):
    queryset = CriminalRecord.objects.all()
    serializer_class = CriminalRecordSerializer
    permission_classes = [IsAuthenticated]  # Any officer can view
    lookup_field = 'id'


class CriminalRecordUpdateView(generics.UpdateAPIView):
    queryset = CriminalRecord.objects.all()
    serializer_class = CriminalRecordSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Admin-only
    lookup_field = 'id'


class CriminalRecordDeleteView(generics.DestroyAPIView):
    queryset = CriminalRecord.objects.all()
    serializer_class = CriminalRecordSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]  # Admin-only
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': 'success',
            'message': 'Criminal record deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
