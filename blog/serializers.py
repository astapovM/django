from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from blog.models import Blog


class BlogModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField()
    photo = serializers.ImageField()
    category = serializers.CharField()


    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


# def encode():
#     model = BlogModel("Новость из Django Rest", "Тестовая запись REST")
#     model_sr = BlogSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)