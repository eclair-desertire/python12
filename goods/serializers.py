from goods.models import Good

from rest_framework import serializers


class GoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Good
        fields = '__all__'
    