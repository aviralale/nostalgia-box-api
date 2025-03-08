from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import FutureMessage
from .serializers import FutureMessageSerializer
from rest_framework import permissions
from rest_framework.decorators import action


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class FutureMessageViewSet(ModelViewSet):
    queryset = FutureMessage.objects.all()
    serializer_class = FutureMessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    @action(detail=False, methods=["GET"])
    def user_future_messages(self, request):
        user_future_messages = self.queryset.filter(created_by=request.user)
        serializer = self.get_serializer(user_future_messages, many=True)
        return Response(serializer.data)
