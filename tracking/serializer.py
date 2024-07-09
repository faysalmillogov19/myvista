from rest_framework import serializers
from panne.models import Panne, Type

class PanneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Panne
		fields = ['id', 'vehicule_id', 'type_id', 'pieces', 'description', 'date','immobile']

