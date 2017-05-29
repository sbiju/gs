from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

#Relative Imports
from .models import Villa
from .serializers import VillaSerializer, VillaListSerializer


# Create View
class VillaCreateApi(CreateAPIView):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    serializer_class = VillaSerializer
    queryset = Villa.objects.all()


# Update View
class VillaUpdateApi(RetrieveUpdateAPIView):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    serializer_class = VillaSerializer
    queryset = Villa.objects.all()


# Delete View
class VillaDeleteApi(RetrieveDestroyAPIView):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    serializer_class = VillaSerializer
    queryset = Villa.objects.all()


# Detail View
class VillaDetailApi(RetrieveAPIView):
    serializer_class = VillaSerializer
    queryset = Villa.objects.all()


# List View
class VillaListApi(ListAPIView):
    serializer_class = VillaListSerializer
    queryset = Villa.objects.all()