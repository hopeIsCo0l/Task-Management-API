from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer, TaskSerializer
from .serializers import TaskSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    # permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'priority_level']
    ordering_fields = ['due_date', 'priority_level']
    # serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ['status', 'priority_level']
    # ordering_fields = ['due_date', 'priority_level']

    def get_queryset(self):
        # Ensure a user sees only their own tasks
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Assign the owner to the task when creating it
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.mark_complete()
        return Response({'status': 'task marked as complete'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        task.mark_incomplete()
        return Response({'status': 'task marked as incomplete'}, status=status.HTTP_200_OK)


