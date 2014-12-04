from django.test import TestCase
from model_mommy import mommy
from snippets.models import Snippet
class SnippetTest(TestCase):

  def setUp(self):
    self.snippet = mommy.make('Snippet')

  def test_snippet_creation(self):
    self.assertTrue(isinstance(self.snippet, Snippet))