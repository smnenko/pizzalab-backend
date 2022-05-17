from rest_framework import serializers

from item.models import Item
from item.models import Caloricity
from category.models import Category
from category.serializers import CategorySerializer


class CaloricitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Caloricity
        fields = (
            'protein',
            'fat',
            'carbohydrate',
            'calories'
        )


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    caloricity = CaloricitySerializer()

    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {'slug': {'required': False}}

    def create(self, validated_data):
        caloricity = validated_data.pop('caloricity', None)
        category_id = validated_data.pop('category_id', None)

        category = Category.objects.get(id=category_id)
        item = Item(**validated_data, category=category)
        item.save()

        Caloricity.objects.create(**caloricity, item=item)

        return item

    def update(self, instance, validated_data):
        caloricity = validated_data.pop('caloricity', None)
        category_id = validated_data.pop('category_id', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if category_id:
            instance.category = Category.objects.get(id=category_id)

        if caloricity:
            for key, value in caloricity.items():
                setattr(instance.caloricity, key, value)

            instance.caloricity.save(update_fields=caloricity.keys())
        instance.save(update_fields=validated_data.keys())
        return instance


class ItemDetailSerializer(ItemSerializer):
    pass
