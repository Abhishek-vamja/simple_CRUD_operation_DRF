"""
Serializer for models.
"""
from rest_framework import serializers

from core.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for student model.
    """
    class Meta:
        model = Student
        fields = '__all__'