from rest_framework import serializers

from models import Teacher


class TeacherSerializer:
    """Class to serialize model Teacher to JSON format."""
    class Meta:
        """Define which attributes should be included at serialization."""
        model = Teacher
        fields = '__all__'
