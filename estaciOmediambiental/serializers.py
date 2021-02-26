from rest_framework import serializers
from estaciOmediambiental.models import Client, Sensor, Registre


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'identificador',
            'localitzacio'
        ]


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = [
            'identificador',
            'client'
        ]


class RegistreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registre
        fields = [
            'hora',
            'valor',
            'sensor'
        ]
