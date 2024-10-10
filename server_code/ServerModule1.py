
import anvil.server

# Example questions
questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "What is the largest ocean?", "choices": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"}
]

@anvil.server.callable
def get_questions():
    return questions

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
