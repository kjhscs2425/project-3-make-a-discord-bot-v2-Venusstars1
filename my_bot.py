import random
state = "start"
random_riddle = None
riddle_1 = " Patricia's parents have three daughters: May, June, and what's the name of the third daughter?"
riddle_2 = " What has a heart but doesn't beat?"
riddle_3 = " Where can you finish a book without finishing a sentence?"
riddle_4 = " What comes once in a minute, twice in a moment, but never in a thousand years?"
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  #print (random_riddle)
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
  if random_riddle == riddle_1:
    return True
  if random_riddle == riddle_2:
    return True
  if random_riddle == riddle_3:
    return True
  if random_riddle == riddle_4:
    return True
  if "countdown" in user_message.lower():
    return True
  if "sarcastic" in user_message or "Sarcastic" in user_message:
    return True
  if state == "waiting_sarcastic":
    return True
  if "backward" in user_message or "Backward" in user_message:
    return True
  if state == "reverse":
    return True
  if "funny" in user_message or "Funny" in user_message:
    return True
  if "dog" in user_message or "Dog" in user_message:
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
  #random_riddle
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
  if "countdown" in user_message.lower():
    countdown = ""
    for i in range (10, 0, -1):
      countdown += str(i) + " "
    return(countdown)
  if "sarcastic" in user_message or "Sarcastic" in user_message:
    state = "waiting_sarcastic"
    return "Please give me a sentence to sarcastify"
  if state == "waiting_sarcastic":
    sarcastic = user_message
    sarcastic = sarcastic.replace("a", "A")
    sarcastic = sarcastic.replace("u", "U")
    sarcastic = sarcastic.replace("e", "E")
    sarcastic = sarcastic.replace("o", "O")
    sarcastic = sarcastic.replace("i", "I")
    state = "start"
    return sarcastic
  if "backward" in user_message or "Backward" in user_message:
    state = "reverse"
    return "what is your message for me?"
  if state == "reverse":
    reverse = user_message[::-1]
    state = "start"
    return reverse
  if "funny" in user_message or "Funny" in user_message:
    return "here is the best dad joke ever. Why couldnt the little boy go see the pirate movie? Because it was rated “Arrrgh!"
  if "dog" in user_message or "Dog" in user_message:
    fact_1 = "dogs sweat through their paws"
    fact_2 = "dogs can get jealous if you display affection to another creature"
    fact_3 = "Three dogs have served as mayors in the city of Idyllwild"
    fact_4 = "All puppies are born deaf"
    list_of_facts = [fact_1, fact_2, fact_3, fact_4]
    random_joke = random.choice(list_of_facts)
    return "Did you know that " + random_joke
  
  if "riddle" in user_message or "Riddle" in user_message:
    list_of_riddles = [riddle_1, riddle_2, riddle_3, riddle_4]
    global random_riddle
    random_riddle = random.choice(list_of_riddles)
    return ("""Would you like a riddle? I shall give you the hardest riddle of them all, one that
the greatest minds have pondered for generations but have not solved. However, I see the brilliant mind in front of me
and I am confident that you will be successful in deciphering this master riddle.   
The riddle is:""" + str(random_riddle))
  if random_riddle == riddle_1:
    if user_message == "Patricia" or user_message == "patricia":
      state = "start"
      return "that is very very impressive, not many have been able to solve this riddle! Congrats! You are officially a mastermind"
    if user_message == "July" or user_message == "july":
      return "sorry that is incorrect, but please try again next time"
    else:
      return "Sadly that is incorrect, but please try again next time"
  if random_riddle == riddle_2:
    if user_message == "artichoke" or user_message == "Artichoke":
      return "That is correct, great job! I am very impressed that you have successfully deciphered this riddle :)"
    else:
      return "Sadly that is incorrect, but please try again next time"
  if random_riddle == riddle_3:
    if user_message == "prison" or user_message == "Prison":
      return "That is correct, great job! I am very impressed that you have successfully deciphered this riddle :)"
    else:
      return "Sadly that is incorrect, but pleast try again next time"
  if random_riddle == riddle_4:
    if user_message == "the letter M" or user_message == "the letter m" or user_message == "m" or user_message == "M":
      return "That is correct, great job! I am very impressed that you have successfully deciphered this riddle :)"
    else:
      return "Sadly that is incorrect, but pleast try again next time"

             
        
#return f"""Hello, you said my name. I have awoken!!
#{user_message.replace("robot", user_message + ",what would you like assistance with?")}"""
