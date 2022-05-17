from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at')

    def get_parent(self, obj):
        return CategorySerializer(obj.parent).data if obj.parent else None
