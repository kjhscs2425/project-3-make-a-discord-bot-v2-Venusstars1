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
    return "It's the ten duel commandments"
  if "Josie" in user_message or "josie" in user_message:
    return "Josie"
  


#return f"""Hello, you said my name. I have awoken!!
#{user_message.replace("robot", user_message + ",what would you like assistance with?")}"""
