state = "start"
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "who lives in a pineapple under the sea" in user_message or "Who lives in a pineapple under the sea" in user_message:
    return True
  if "capitalize" in user_message or "Capitalize" in user_message:
    return True
  if "1,2,3,4,5,6,7,8,9" in user_message or "123456789" in user_message:
    return True
  if "Josie" in user_message or "josie" in user_message:
    return True
  if state == "waiting_capitalized":
    return True
  if state == "waiting_lowercase":
    return True
  if "lower" in user_message or "Lower" in user_message:
    return True
  if "Knock Knock" in user_message or "knock knock" in user_message or "Knock knock" in user_message:
    return True
  if state == "waiting_joke":
    return True
  if state == "joke_response":
    return True
  if "riddle" in user_message or "Riddle" in user_message:
    return True
  if state == "waiting_riddle":
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global state
  if "who lives in a pineapple under the sea" in user_message or "Who lives in a pineapple under the sea" in user_message:
    return "Spongebob Square Pants!!!"
  if "capitalize" in user_message or "Capitalize" in user_message:
    state = "waiting_capitalized"
    return "What would you like me to capitalize?"
  if state == "waiting_capitalized":
    capitalized_message = user_message.upper()
    state = "start"
    return capitalized_message
  if "1,2,3,4,5,6,7,8,9" in user_message or "123456789" in user_message:
    return "It's the ten duel commandments!!!"
  if "Josie" in user_message or "josie" in user_message:
    return "Josie's on a vacation far away, come around and talk it over!"
  if "lower" in user_message or "Lower" in user_message:
    state = "waiting_lowercase"
    return "What would you like me to lowercase?"
  if state == "waiting_lowercase":
    lowercase_message = user_message.lower()
    state = "start"
    return lowercase_message
  if "Knock Knock" in user_message or "knock knock" in user_message or "Knock knock" in user_message:
    state = "waiting_joke"
    return "Who's there?"
  if state == "waiting_joke":
    state = "joke_response"
    return (user_message + """ who?
            

Wait, I do not understand the joke, please explain it to me""")
  if state == "joke_response":
    state = "start"
    return "Haha, good one! You really got me with that one, keep up the funny humor! :)"
  if "riddle" in user_message or "Riddle" in user_message:
    state = "waiting_riddle"
    return """Would you like a riddle? I shall give you the hardest riddle of them all, one that
the greatest minds have pondered for generations but have not solved. However, I see the brilliant mind in front of me
and I am confident that you will be successful in deciphering this master riddle. 

The riddle is: Patricia's parents have three daughters: May, June, and what's the name of the third daughter?"""
  if state == "waiting_riddle":
    state = "start"
    if user_message == "Patricia" or user_message == "patricia":
      return "that is very very impressive, not many have been able to solve this riddle! Congrats! You are officially a mastermind"
    if user_message == "July" or user_message == "july":
      return """I thought you were a mastermind, but clearly I was mistaken. 
You are as foolish as those who came before you, tricked by such a simple misdirection. 
Try again next time and when you do, ask someone else who is wiser than you! What a foolish fool"""
    else:
      return "Sadly that is incorrect, but please try again next time"
  
#Make the riddles randomized
#make a thing that just switches out a word
#Use random library
#string slicing
#for loop


#return f"""Hello, you said my name. I have awoken!!
#{user_message.replace("robot", user_message + ",what would you like assistance with?")}"""
