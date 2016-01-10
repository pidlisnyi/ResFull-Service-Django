from .models import Blat
from rest_framework import serializers


class BlatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blat
        field = ('created_by', 'text')
