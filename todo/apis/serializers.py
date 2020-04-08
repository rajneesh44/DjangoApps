from rest_framework import serializers
from todomain import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'content',
                  )
        model = models.TodoItems
