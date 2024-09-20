import re
import random

class RuleBot:
  ### Potential Negative Responses
  Negative_responses = ("no","nope","nah","na","not a chance","sorry")
  ### Exit Converstion Keywords
  exit_commands = ("quit","pause","exit","goodbye","bye","later")
  ### Random Starter Question
  random_questions = (
        "Why are you here ?",
        "Are there many humans like you ?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader ?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent':r'.*\s*your planet.*',
                            'answer_why_intent' :r'.*\s*why',
                            'about_btech':r'.*\s*btech',
                            'about_computer': r'.*\s*computer'
                            }

  def greet(self):
        self.name = input("what is you name?\n")
        will_help = input (
            f"Hi {self.name}, I am Rule-Bot. Will you help me learn about your planet?\n")
        if will_help in self.Negative_responses :
            print("Ok, have a nice Earthn day!")
            return
        self.chat()

  def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
              print("Okay, have a nice Earth day!")
              return True

  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

  def match_reply (self , reply):
        for key, value in self.alienbabble.items():
          intent = key
          regex_pattern = value
          found_match = re.match(regex_pattern, reply)
          if found_match and intent == 'describe_planet_intent':
              return self.describe_planet_intent()
          elif found_match and intent=='answer_why_intent':
              return self.answer_why_intent()
          elif found_match and intent=='about_btech':
              return self.about_btech()
          elif found_match and intent == 'about_computer':
              return self.about_computer()
        if not found_match:
            return self.no_match_intent()

  def describe_planet_intent(self):
       responses = ("My planet is a utopia of diverse organisms and species.\n",
                    "I am from Opidious , the capital of the wayward Galaxies. \n")
       return random.choice(responses)

  def answer_why_intent(self):
       responses = ("I am in peace\n","I am here to collect data on your planet and its inhabitants\n",
                    "i heard the coffee is good\n")
       return random.choice(responses)

  def about_btech(self):
       responses = ("Bachelor of Technology (B.Tech) degree\n",
                    "The field of engineering and technology\n"
                    "This is a four-year undergraduate degree \n")
       return random.choice(responses)

  def about_computer(self):
       responses = ("A computer is a machine that can be programmed\n",
                    "It carry out sequences of arithmetic or logical operations (computation) automatically\n ")
       return random.choice(responses)

  def no_match_intent(self):
       responses = ("Please tell me more.\n","Tell me more!\n","Why do you say that ?\n", "I see , Can you elaborate?\n",
                    "Interesting. Can you tell me more?\n","I see \n","Why?\n",
                    "How do you think ?\n")
       return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet()