from goods.models import Good, Category

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Good
        fields = '__all__'
    