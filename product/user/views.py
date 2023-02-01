from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class UserDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
