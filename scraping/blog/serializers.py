from rest_framework import serializers
from blog import models

class IndiaTodaySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Title
        fields = ('Heading',)

