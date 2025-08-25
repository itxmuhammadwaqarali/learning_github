from rest_framework import serializers
from .models import Person, color
import re

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()      
class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = color
        fields = ['name']
class PeopleSerializer(serializers.ModelSerializer):
    colors = colorSerializer()  # Nested serializer to include color details
    country = serializers.SerializerMethodField()  # Default country field
    class Meta:
        model = Person
        fields = '__all__'  # This will include all fields from the Person model
        # depth = 1  # To include related color details

    def get_country(self, obj):
        return "Pakistan"  # Default country value 

    def validate_age(self, data):
        if data < 18:
            raise serializers.ValidationError("Age must be at least 18")
        return data
    
    def validate_email(self, data):
        if "@" not in data:
            raise serializers.ValidationError("Invalid email address")
        if Person.objects.filter(email=data).exists():
            raise serializers.ValidationError("Email already exists")

        return data
    
    def validate_name(self, data):
        if not re.match("^[A-Za-z ]+$", data):
            raise serializers.ValidationError("Name must contain only letters and spaces")
        return data