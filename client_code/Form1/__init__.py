# In the Form1 script in Anvil

from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.questions = [
      {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin"], "answer": "Paris"},
      {"question": "What is 2 + 2?", "choices": ["3", "4", "5"], "answer": "4"},
      {"question": "What is the capital of Japan?", "choices": ["Tokyo", "Beijing", "Seoul"], "answer": "Tokyo"}
    ]

  def button_submit_click(self, **event_args):
    selected = self.radio_group_answers.selected_value
    if selected == self.questions[self.current_question]["answer"]:
      self.score += 1
    self.current_question += 1
    if self.current_question < len(self.questions):
      self.show_question()
    else:
      self.label_question.text = f"Quiz finished! Your score is {self.score} out of {len(self.questions)}."
      self.radio_group_answers.items = []
      self.button_submit.enabled = False
