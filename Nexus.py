import random
import webbrowser
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

responses = {
  "hi": ["Hello!", "Hi there!", "Hey!"],
  "how are you?": ["I'm doing well, thanks for asking.", "I'm fine, thanks."],
  "what's your name?": ["My name is Nexus.", "I'm Nexus."],
  "how old are you?" : ["I cannot age, I am a ChatBot",\
                        "As a coded software I do not age."],
  "what is the time" : ["Current Time =", current_time]
}

def handle_user_input(user_input):
    if user_input.startswith("google"):
        query = user_input.split(" ", 1)[1]
        if not query:
            return "Please provide a search query after 'google'."
        search_url = "https://www.google.com/search?q=" + query
        webbrowser.open(search_url)
        return "Here are the Google search results for '{}'. ".format(query)
    elif user_input == "bye":
        return "Nexus: Are you sure you want to exit? (yes/no)"
    else:
        if user_input in responses:
            response = random.choice(responses[user_input])
            return response
        else:
            return "I'm sorry, I didn't understand what you said. You can say 'hi',\
            'how are you?', 'what's your name?' or 'google <query>'."

def chatbot():
  print("Nexus: Hi! I'm Nexus. How can I help you?")
  while True:
      try:
          user_input = input("You: ").lower()
          response = handle_user_input(user_input)
          if response == "Nexus: Are you sure you want to exit? (yes/no)":
              confirm_exit = input(response).lower()
              if confirm_exit == "yes":
                  print("Nexus: Goodbye!")
                  break
              else:
                  print("Nexus:", response)
          else:
              print("Nexus:", response)
      except Exception as e:
          print("An error occurred:", str(e))

if __name__ == "__main__":
  chatbot()