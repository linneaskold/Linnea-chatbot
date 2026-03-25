import random
#Rulest: list of (keywords, respones)
rules = [
#greetings
(["hello", "hi", "hey"], [
    "Hello!, how are you feeling today?",
    "Hi!, What makes you want to talk to me today?",
    "Hi! tell me something thats been on your mind lately!",
    "Hello there, tell me something interesting that have happend today",
    "Good day my friend, tell me something about your day"
    ]),


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
 


farewell_words = ["bye", "byee", "goodbye", "see you"]



def run_zeta():
    print("Hello, I am a bot named Zeta. Is there anything you want to talk about today?")
    print("if you no longer wish to talk to me just type bye")
    


run_zeta()





def main():


    run_zeta()



while True:
    user = input("You: ")
    user = user.lower()
    found = False

    for keywords, responses in rules:
        if any(word in user for word in keywords):
                answer = random.choice(responses)
                print("bot:", answer)
                found = True
                break
            
        if found:
               break



    if not found:
       print("bot:", random.choice(fallback))



    if any(word in user for word in farewell_words):
       break
   
    if __name__ == "__main__":
       main()


