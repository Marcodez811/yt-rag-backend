from rest_framework import serializers
from obot_api.models import Course
from users.models import UserAccount


class CourseSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=150)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=UserAccount.objects.all())

    class Meta:
        model = Course
        fields = ['course_id', 'name', 'owner', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Course` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
