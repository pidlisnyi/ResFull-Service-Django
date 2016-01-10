from .models import Blat
from .serializers import BlatSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class BlatList(APIView):

    def get(self, request, format=None):
        blats = Blat.objects.filter(created_by__is_active=True)
        serialized_blats = BlatSerializers(blats, many=True)
        return Response(serialized_blats.data)


class BlatDetails(APIView):

    def get_object(self, pk):
        try:
            return Blat.objects.get(pk=pk)
        except Blat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blat = self.get_object(pk)
        serialized_blat = BlatSerializers(blat)
        return Response(serialized_blat.data)
