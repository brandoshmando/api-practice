from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Snippet
    fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language' 'style')
  owner = serializers.Field(source='owner.username')
  highlight = serializers.HyperlinkedIdentityField(view_name='highlight', format='html')

  def create(self, validated_attrs):
    """
    Create and return a new 'Snippet' instance, given the validated data.
    """
    return Snippet.objects.create(**validated_attrs)

  def update(self, instance, validated_attrs):
    """
    Update and return existing 'Snippet' instance, given the validated data
    """

    instance.title = validated_attrs.get('title', instance.title)
    instance.code = validated_attrs.get('code', instance.code)
    instance.linenos = validated_attrs.get('linenos', instance.linenos)
    instance.language = validated_attrs.get('language',instance.language)
    instance.style = validated_attrs.get('style', instance.style)
    instance.save()
    return instance

class UserSerializer(serializers.ModelSerializer):
  snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', queryset=Snippet.objects.all())

  class Meta:
    model = User
    fields = ('url', 'username', 'snippets')