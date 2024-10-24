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
    self.current_question = 0
    self.score = 0

    def display_question(self):
        if self.question_index < len(self.questions):
            q = self.questions[self.question_index]
            self.label_question.text = q['question']
            self.radio_button_1.text = q['choices'][0]
            self.radio_button_2.text = q['choices'][1]
            self.radio_button_3.text = q['choices'][2]
            self.radio_button_4.text = q['choices'][3]
            self.label_score.text = f"Score: {self.score}"
        else:
            self.label_question.text = f"Quiz Complete! Your final score: {self.score}"
            self.radio_button_group.visible = False
            self.button_submit.visible = False
            anvil.server.call('save_quiz_result', self.score, self.user_id)

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
