from rest_framework import serializers


class EmptySerializer(serializers.Serializer):
    """
    A special class for views without serializers to represent them in swagger
    """
    pass
