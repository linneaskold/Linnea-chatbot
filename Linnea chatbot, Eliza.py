import random

rules = [
#greetings
(["hello", "hi", "hey"], [
    "Hello!, how are you feeling today?",
    "Hi!, What makes you want to talk to me today?",
    "Hi! tell me something thats been on your mind lately!",
    "Hello there, tell me something interesting that have happend today",
    "Good day my friend, tell me something about your day"
    ]),

 #happy
(["happy", "joyful", "cheerful", "delighted"], [
    "Thats great to hear!, anything else you want to tell me?",
    "Thats wonderful, tell me more about it!",
    "Tell me everything about why you feel so good, I can be here all day writing to you",
    "Its really fun to hear that you´re doing great lately!"
    ]),

#family
(["mother", "mom", "father", "dad", "sister", "brother"], [
    "Tell me more about your family!",
    "Interesting, tell me something fun you did together",
    "That sounds really fun, tell me more about them!"
    ]),


([])

#pets
(["dog", "cat", "hamster", "rabbit", "bunny"], [
    "You have a pet?, how fun!, tell me more about them",
    "Tell me something interesting about your pet!"
    "It must be really fun having a pet, can they do any tricks?"
    ]),

#kan man lägga till en joke med djuret?


#animals
#"yes"
#"no"


#bye
(["bye", "byee", "goodbye", "see you"],[
    "Bye, hope you have a wonderful day!",
    "Bye, hope we can talk to eachother again sometime",
    "Bye, thank you for talking to me",
    "Bye-bye, have a nice day!",
    "Thank you for chatting with me today, have a nice day!"
    ]),
]

   #fallback answers if keywords not found
fallback = [
    "Tell me more about something you like!",
    "I dont really understand you, explain more so that I can understand!",
    "I dont have knowledge about that, tell me about something else!",
    "Sorry I dont have a answer to that in my program"
    ]

while true:

    user = input("You: ")
    user = user.lower()
    found = False

    for keyword in responses:
        if keyword in user:
            random.choice(responses[keyword])
            print("bot:", answer)
            found = True

            if any(word in user_input.lower() for word in farewell)
            break

        if not found:
            print random.choice(fallback)
        
            
    def run_zeta():
        print("Hello, I am a bot named Zeta. Is there anything you want to talk about today?")
        print("if you no longer wish to talk to me just type "bye":)")

     farewell_words = ["bye", "byee", "goodbye", "see you"]
        run_zeta()




