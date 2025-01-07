from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from .models import Note
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # Anyone can access

class NoteCreateList(generics.ListCreateAPIView):
    # queryset = Note.objects.all() # You can comment this out given that you append the get_queryset method
    serializer_class = NoteSerializer
    permission_classes =  [IsAuthenticated] #Only accessible with valid token
     
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
        # return super().get_queryset()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    # queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)