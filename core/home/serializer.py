from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'  # This will include all fields from the Person model

    def validate_age(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return data