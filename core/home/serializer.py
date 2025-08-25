from rest_framework import serializers
from .models import Person, color
import re

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = color
        fields = ['id', 'name']  # include id too


class PeopleSerializer(serializers.ModelSerializer):
    colors = serializers.PrimaryKeyRelatedField(
        queryset=color.objects.all(), write_only=True
    )  # Accept color as ID when writing
    color_detail = colorSerializer(source='colors', read_only=True)  # Show nested detail on read
    country = serializers.SerializerMethodField()  

    class Meta:
        model = Person
        fields = '__all__'  
        extra_fields = ['color_detail', 'country']

    def get_country(self, obj):
        return "Pakistan"  

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
