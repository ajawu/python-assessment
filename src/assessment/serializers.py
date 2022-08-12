from rest_framework import serializers


class DateOfBirthSerializer(serializers.Serializer):
    dob = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'], required=True)
