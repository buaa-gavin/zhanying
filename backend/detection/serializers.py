from rest_framework import serializers



class PersonListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_blank=True,max_length=255)
    birth = serializers.DateField()