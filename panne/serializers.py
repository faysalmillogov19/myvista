from rest_framework import serializers
from .models import Panne

class PanneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Panne
		fields = ['id', 'vehicule', 'type', 'pieces', 'description', 'date','immobile']

