from rest_framework import generics
from rest_framework.response import Response
from .models import Pill, Reminder
from .serializers import PillSerializer, ReminderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CheckReminder(APIView):
    def get(self, request):
        # Lógica para manejar una solicitud GET
        return Response({"mensaje": "Esta es la página de chequeo de recordatorios."})


class PillListCreate(generics.ListCreateAPIView):
    queryset = Pill.objects.all()
    serializer_class = PillSerializer

class ReminderListCreate(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        try:
            instance = serializer.save()
            if instance.is_time_to_take_pill():
                return Response({"message": "¡Es hora de tomar la pastilla!"}, status=200)
            else:
                return Response({"message": "Recordatorio creado con éxito."}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
