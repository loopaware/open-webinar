from rest_framework import serializers
from .models import Attendee, Setting, Speaker, AgendaItem

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['key', 'value', 'description']

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ['id', 'name', 'role', 'bio', 'image', 'order']

class AgendaItemSerializer(serializers.ModelSerializer):
    speaker_name = serializers.ReadOnlyField(source='speaker.name')
    
    class Meta:
        model = AgendaItem
        fields = ['id', 'time', 'title', 'description', 'speaker', 'speaker_name', 'order']

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['id', 'name', 'email', 'company', 'experience', 'date', 'image_url']
        read_only_fields = ['id', 'image_url']