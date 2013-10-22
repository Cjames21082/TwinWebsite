"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Question, Choice


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class QuestionMethodTests(TestCase):

	def test_was_published_with_future_date(self):
		""" 
		was_published_recently() should return False for question 
		whose pub_date is in the future. """

		time = timezone.now() + datetime.timedelta(days = 30)
		future_question = Question(pub_date = time)
		self.assertEqual(future_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):

		""" 
		was_published_recently() should return True for questions 
		whose pub_date is within the last day. """

		time = timezone.now() - datetime.timedelta(hours = 1)
		recent_question = Question(pub_date = time)
		self.assertEqual(recent_question.was_published_recently(), True)

def create_question(question_text, days):
	""" 
	Creates a quesiton with the given 'question_text' published the given
	number of 'days' offset to now (negative for questions published 
	in the past, positive for questions that have yet to be published). """

	time = timezone.now() + datetime.timedelta(days = days)
	return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionViewTests(TestCase):

	def test_index_view_with_no_questions(self):
		"""
		If no questions exist, an appropriate message should be displayed. """

		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_a_past_question(self):
		"""
		Questions with a pub_date in the past should be displayed on
		the index page. """

		create_question(question_text = "Past question", days = -30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], 
			['<Question: Past question>'])

	def test_index_view_with_a_future_question(self):
		""" Questions with a pub_date in the future should not be displayed
		on the index page."""

		create_question(question_text = "Future question.", days = 30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, 'No polls are available', status_code = 200)
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_with_future_question_and_past_question(self):
		""" Even if both past and future questions exist, only past questions 
		should be displayed. """

		create_question(question_text = "Past question.", days = -30)
		create_question(question_text = "Future question.", days = 30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], 
								['<Question: Past question.>'])

	def test_index_view_with_two_past_questions(self):
		""" 
		The questions index page may display multiple questions. """

		create_question(question_text = "Past question1.", days = -30)
		create_question(question_text = "Past question2.", days = -5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
				 response.context['latest_question_list'],
				 ['<Question: Past question2.>', '<Question: Past question1.>'])

class QuestionIndexDetailTests(TestCase):

	def test_detail_view_with_a_future_question(self):
		""" The detail view of a question with a pub_date in the future 
		should return a 404 not found """

		future_question = create_question(question_text = "Future question.", days = 5)
		response = self.client.get(reverse('polls:details', args = (future_question.id,)))
		self.assertEqual(response.status_code, 404)

	def test_detail_view_a_past_question(self):
		""" The detail view of a question with a pub_date in the past should
		display the question's text. """

		past_question = create_question(question_text = "Past question.", days = -5)
		response = self.client.get(reverse('polls:details', args = (past_question.id,)))
		self.assertContains(response, past_question.question_text, status_code = 200)

		


