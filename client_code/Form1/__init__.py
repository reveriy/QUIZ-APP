from ._anvil_designer import Form1Template
import anvil.server

class Form1(Form1Template):

    def __init__(self, **properties):
        self.init_components(**properties)
        self.question_index = 0
        self.score = 0
        self.questions = anvil.server.call('get_questions')
        self.user_id = "example_user_id"  # Replace with real user identification
        self.display_question()

    # Display questions and options
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

    # Handle the button click event
    def button_submit_click(self, **event_args):
        q = self.questions[self.question_index]
        selected_choice = self.radio_button_group.selected_value
        if selected_choice == q['answer']:
            self.score += 1
        self.question_index += 1
        self.display_question()

    # Method placeholder for radio button clicks
    def radio_button_clicked(self, **event_args):
        pass

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass

    def radio_button_1_clicked(self, **event_args):
      """This method is called when this radio button is selected"""
      pass

    def radio_button_2_clicked(self, **event_args):
      """This method is called when this radio button is selected"""
      pass

    def radio_button_3_clicked(self, **event_args):
      """This method is called when this radio button is selected"""
      pass

    def radio_button_4_clicked(self, **event_args):
      """This method is called when this radio button is selected"""
      pass
