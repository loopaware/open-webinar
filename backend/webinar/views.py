import os
from django.conf import settings
from django.shortcuts import redirect
from django.core.files.base import ContentFile
from inertia import render
from rest_framework import status, views, permissions
from rest_framework.response import Response
from .models import Attendee, Speaker, AgendaItem, Setting
from .serializers import AttendeeSerializer, SpeakerSerializer, AgendaItemSerializer, SettingSerializer
from .utils import generate_mushroom
import logging

logger = logging.getLogger(__name__)

class IndexView(views.APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        speakers = Speaker.objects.all()
        agenda = AgendaItem.objects.all()
        settings_queryset = Setting.objects.all()
        
        # Convert settings to a dict for easier frontend use
        settings_dict = {s.key: s.value for s in settings_queryset}
        
        return render(request, 'App', props={
            'speakers': SpeakerSerializer(speakers, many=True).data,
            'agenda': AgendaItemSerializer(agenda, many=True).data,
            'settings': settings_dict,
            'new_attendee': request.session.pop('new_attendee', None)
        })

class RegisterAttendeeView(views.APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [] 

    def post(self, request):
        serializer = AttendeeSerializer(data=request.data)
        if serializer.is_valid():
            attendee = serializer.save()
            
            try:
                # Generate mushroom art in-memory
                image_buffer = generate_mushroom(attendee.id)
                image_filename = f"attendee_mushroom_{attendee.id}.png"
                
                # Save to ImageField (handles S3/MinIO upload automatically)
                attendee.image.save(image_filename, ContentFile(image_buffer.read()), save=True)
                
                request.session['new_attendee'] = AttendeeSerializer(attendee).data
                return redirect('index')
            except Exception as e:
                logger.error(f"Art generation failed: {e}")
                request.session['new_attendee'] = AttendeeSerializer(attendee).data
                return redirect('index')
        
        # Re-fetch data for errors page
        speakers = Speaker.objects.all()
        agenda = AgendaItem.objects.all()
        settings_queryset = Setting.objects.all()
        settings_dict = {s.key: s.value for s in settings_queryset}

        return render(request, 'App', props={
            'errors': serializer.errors,
            'speakers': SpeakerSerializer(speakers, many=True).data,
            'agenda': AgendaItemSerializer(agenda, many=True).data,
            'settings': settings_dict,
        })

class ListAttendeesView(views.APIView):
    def get(self, request):
        auth_header = request.headers.get('X-Admin-Password')
        if auth_header != settings.ADMIN_PASSWORD:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
            
        attendees = Attendee.objects.all().order_by('-id')
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)