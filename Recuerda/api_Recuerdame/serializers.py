from rest_framework import serializers
from django.utils import timezone  # Importar timezone aquí
from .models import Pill, Reminder

class PillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pill
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    pill_name = serializers.CharField(source='pill.name', read_only=True)
    
    class Meta:
        model = Reminder
        fields = '__all__'

    def validate_reminder_time(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("La hora del recordatorio debe ser en el futuro.")
        return value
