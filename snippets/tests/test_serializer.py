from django.test import TestCase
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import serializers
from model_mommy import mommy

class TestSnippetSerializer(TestCase):
  def setUp(self):
    self.snippet = mommy.make('Snippet')

  def test_creation_of_snipppet_serializer(self):
    self.assertTrue(isinstance(SnippetSerializer(self.snippet), SnippetSerializer))