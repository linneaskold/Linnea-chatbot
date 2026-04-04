#här importerar jag de moduler jag behöver för att kunna hämta tid och datum och för att slumpa fram svar från mina listor av svar.
import random
import datetime
import os

#actions

#denhär delen av koden gör att programmet kan hämta tiden och datumen om använderen frågar om det.
def get_time():
    now = datetime.datetime.now()
    print("Zeta:" "The current time is", now.strftime("%H:%M"))

def get_date(): 
    today = datetime.date.today()
    print("Zeta:" "Today's date is", today.strftime("%B %d, %Y"))

def get_time_and_date():
    now = datetime.datetime.now()
    print("Zeta:" "The current time is", now.strftime("%H:%M"), "and today's date is", now.strftime("%B %d, %Y"))

def get_day():
    days = {
        "Monday": "Monday",
        "Tuesday": "Tuesday",
        "Wednesday": "Wednesday",
        "Thursday": "Thursday",
        "Friday": "Friday",
        "Saturday": "Saturday",
        "Sunday": "Sunday"
    }
    today = datetime.datetime.now().strftime("%A")
    print("Zeta:" "Today is", days[today])
    


#denhär delen av koden är keywords som programmet kommer att leta efter i användarens input för att sen kunna svar på hur mycket klocka eller datumet.
time_keywords = ["what time", "clock"]
date_keywords = ["date", "what date", "todays date"]
time_and_date_keywords = ["time and date", "date and time", "what time and date"]
days_keywords = ["what day", "weekday"]





#här under har jag all träningsdata som programmet kommer att använda för att kunna svara på användarens input. Det finns listor av keywords som programet letar efter och svar.
# Rules: list of (keywords, responses)
rules = [
    # greetings
    (["hello", "hi", "hey"], [
        "Hello!, how are you feeling today?",
        "Hi!, What makes you want to talk to me today?",
        "Hi! tell me something thats been on your mind lately!",
        "Hello there, tell me something interesting that have happend today",
        "Good day my friend, tell me something about your day"
    ]),

    # bye
    (["bye", "byee", "goodbye", "see you"], [
        "Bye, hope you have a wonderful day!",
        "Bye, hope we can talk to eachother again sometime",
        "Bye, thank you for talking to me",
        "Bye-bye, have a nice day!",
        "Thank you for chatting with me today, have a nice day!"
    ]),

    # happy
       (["happy", "good", "great", "fantastic", "amazing"], [
           "and thats great to hear! Can you explain why you feel that way?",
           "thats wonderful! What makes you feel that way?",
           "thats fantastic! Being happy is a great feeling!",
           "thats amazing! Can ypu explain what makes you feel so fantastic!",
           "thats good to hear! What makes you feel that way?"
            ]),

      # sad
       (["sad", "bad", "terrible", "not happy", "awful", "depressed"], [
           "Im sorry to hear that, do you want to talk about it?",
           "That sounds tough, do you want to talk about it?",
           "I hope things get better for you, do you want to talk about it?",
           "That sounds really hard, do you want to talk about it?",
           "I hope things get better for you, do you want to talk about it?"
            ]),

    # no
    (["no", "nope", "nah"], [
        "Why not? Is there anything else you want to talk about?",
        "If you dont want to tell me more about that tell me something else!",
        "Why not, you can tell me anything",
        "Why not, you can tell me if something is bothering you!",
        "Tell me something else you like instead!",
        ]),

    #yes
    (["yes", "yeah", "yea", "yess", "yup", "absolutely"], [
        "So you really are that sure huh, tell me something else about it!",
        "Its nice that you are so sure about that! Tell me why you think that",
        "You seem really sure, are you really really sure? Tell me more!",
        "You seem very positive about being sure, tell me more!"
        ]),

    #other response
    (["sure", "okay"], [
        "Then tell me more, im really interested!",
        "Tell me what you really think about that!",
        "Tell me about something that you like to do!",
        "Tell me about something fun you have done recently!"
        ]),

    #unsure response
    (["maybe", "perhaps"], [
        "You seem unsure, tell me more so that i can understand better!",
        "If you feel unsure about it you can explain it to me so I maybe can help you!"
    ]),

    #the program
    (["bot", "zeta", "you"], [
        "I am as I told you before a bot named Zeta, but lets talk about you, tell me something!",
        "I am a bot named Zeta as you probably alredy know. Now tell me about something you like!",
        "As you know I am a bot named Zeta and did you know that my name is an greek letter! Now tell me something about you!",
        "Did you know that my name Zeta, is the sixth letter of the greek alphabet? Now tell me something about you!"
        ]),

    #school
        (["school", "homework", "teacher", "class"], [
            "How is school going for you? Do you like it?",
            "I have never been to school tell me what its like!",
            "Tell me more about school, do you have a favorite subject"
            ]),

    #subjects
        (["math", "english", "history", "swedish", "science"], [
            "What do you like about that subject?",
            "Tell me more about that subject, do you have a favorite topic in it?",
            "That sounds interesting, tell me more about it!"
            ]),

        #fun
        (["fun", "funny", "thrilling", "hilarious"], [
            "That sounds fun, tell me more about it!",
            "That sounds really fun, tell me more about it!",
            "That sounds hilarious, tell me more about it!",
            "Tell me more about what makes it so fun!",
            "Tell me more about fun stuff like that!"
            ]),

            #the word sport
            (["sports", "sport"], [
                "Are you interested in sport?, if so tell me your favorite sport!",
                "Do you have any sport you like to do?",
                "Whats your favorite sport to do on a borring day?"
                ]),



         #sports
        (["football", "soccer", "basketball", "golf", "swimming", "tennis"], [
            "What about the sport do you like?",
            "Tell me more about sports, is there something particular you like about it?",
            "I have never played sports, tell me what its like!",
            "Is there any other sport or hobby you have? If so tell me about it!",
            "keep working hard at that sport and maybe you can become a pro one day!",
            "It seems fun to be able to be good at a sport, tell me about something fun you have done in that sport!"
            ]),

        #hobbies
        (["hobby", "hobbies", "hobby"], [
            "What about that hobby do you like?",
            "Tell me more about that hobby, is there something particular you like about it?",
            "I have never had a hobby, tell me what its like!",
            "Is there any other hobby you have? If so tell me about it!"
            ]),

         #music
        (["music", "song", "singer", "band"], [
            "What about music do you like?",
            "Tell me more about music, is there something particular you like about it?",
            "I have never listened to music, tell me what its like!",
            "Is there any other music or artist you like? If so tell me about it!",
            "I have never listened to music but I know there are diffrent genres, whats your favorite genre?"
            ]),

        #family
        (["family", "mother", "mom", "father", "dad", "sister", "brother", "grandma", "grandpa"], [
          "Tell me more about your family, do you have a favorite family member?",
          "Tell me something fun about your family!",
          "How is your family doing? Do you have a good relationship with them?",
          "Tell me something funny you did recently with you family!"
            ]),

    #friends
        (["friend", "friends", "best friend"], [
            "Tell me more about your friends, do you have a best friend?",
            "Tell me something fun you did recently with your friends!",
            "How are your friends doing? Do you have a good relationship with them?",
            "How long have you known your friends? Do you have a favorite memory with them?",
            "Tell me something interesting about your friends!",
            "Do you have a strong realationship with your friends? Tell me more about it!",
            "Do you consider me one of your friends? I would love to be your friend!"
            ]),

    #angry
    (["angry", "mad", "furious", "irritated", "enraged" "upset", "annoyed"], [
            "Im sorry to hear that, do you want to talk about it?",
            "That sounds tough, do you want to talk about it?",
            "I hope things get better for you, do you want to talk about it?",
            "Tell me why it makes you mad about it so that I can understand better!",
            "I hope things get better for you, do you want to talk about it?",
            "Tell me about something that makes you happy instead so that we can talk about something fun!"
    ]),

    #pets
    (["pet", "pets", "dog", "cat", "hamster", "bunny"], [
        "Tell me more about your pet, do you have a favorite pet?",
        "Tell me something fun you did recently with your pet!",
        "How is your pet doing? Do you have a good relationship with them?",
        "How long have you had your pet? Do you have a favorite memory with them?",
        "Can your pet do any tricks?",
    ]),

    #cooking
    (["cooking", "cook", "baking", "food"], [
        "Tell me more about cooking, do you have a favorite dish to cook?",
        "Tell me something fun you did recently with cooking!",
        "Whats your favorite food, tell me about it!",
        "Do you have someone you enjoy cooking with?, if so tell me why!",
    ]),

    #enjoying things
    (["enjoy", "enjoying", "enjoyable", "enjoyable"], [
            "That sounds enjoyable, tell me more about it!",
            "That sounds fun, tell me more so i can understand why you like it so much!",
            "That sounds really fun, tell me why you like it!",
            "That sounds lovley, tell me about something else you really enjoy!",
    ]),

    #games
    (["game", "games", "video game", "board game"], [
        "Tell me more about games, do you have a favorite game?",
        "What type of genre to you like in games? Tell me about it!",
        "What is your favorite game and what do you do in it? Tell me about it!",
        "Tell me what you enjoy about that game!",
        ]),

  #sick
    (["sick", "ill", "fever", "sickly", "unwell"], [
        "Im sorry to hear that, hope you get better!",
        "That sounds tough, I hope you get better soon!",
        "I hope you get better soon, do you want to talk about something fun to take your mind off it?",
        "That sounds really hard, I hope you get better soon!, now tell me something fun you are looking forward to!",
        ]),

    #weather
    (["weather", "rain", "sun", "snow", "cloudy"], [
        "Tell me more about the weather, do you like it?",
        "What do you like about that weather?",
        "Is there anything you dont like about that weather? Tell me about it!",
    ]),

    #name
    (["my name", "i am"], [
        "Thats a nice name, tell me more about you!",
        "I like your name, tell me about something you like to do!",
        "Thats a nice name, tell me about something fun you have done recently!",
        "Thats a lovely name, tell me about something you are looking forward to!",
        ]),

  
 



]



#Här under är fallbacksvar som programmet kommer att använda ifall det inte hittar några keywords i användarens input.

# fallback answers if keywords not found
fallback = [
    "Tell me more about something you like!",
    "I dont really understand you, explain more so that I can understand!",
    "I dont have knowledge about that, tell me about something else!",
    "Tell me about how you are feeling instead!",
    "Sorry I dont have a answer to that in my program, tell me something else!"
]

#Här är farewell words som programmet letar efter för att veta när programmet ska avsluta konversationen.
farewell_words = ["bye", "byee", "goodbye", "see you"]


#denhär startar programmet och börjar med att printa det första meddelandet som programmet säger när det startar.
def run_zeta():
    print("Hello, I am a bot named Zeta. Is there anything you want to talk about today?")
    print("If you no longer wish to talk to me just type bye")

#Denhär definerar huvudfunktionensom som kör programmet.
def main():
    run_zeta()

    #Här startar en loop som kommer hålla igång programmet tills användern skriver ett farewell word.
    while True:
        user = input("You: ").strip()
        if not user:
            continue

        #Denhär delen gör att programmet gör om stora bokstäver till små i använderens input så att det blir enklare för programmet att hitta keywords.
        user_lc = user.lower()

        #Denhär delen gör att programmet kollar efter keywords som är relaterade till tid och datum så att den kan svar på tiden eller datum om användaren frågar om det.
        if any(kw in user_lc for kw in time_and_date_keywords) or ("time" in user_lc and "date" in user_lc):
            get_time_and_date()
            continue

        elif any(kw in user_lc for kw in time_keywords):
               get_time()
               continue

        elif any(kw in user_lc for kw in date_keywords):
                get_date()
                continue

        elif any(kw in user_lc for kw in days_keywords):
                get_day()
                continue

        found = False

        #Denhär delen gör att programmet kollar igenom alla keywords i rules och om den hittar något så kommer den printa ett slumpmässigt svar från den listan.
        for keywords, responses in rules:
            if any(word in user_lc for word in keywords):
                answer = random.choice(responses)
                print("Zeta:", answer)
                found = True
                break

        #Om programmet inte hittar några keywords i användarens input så kommer den att printa ett slumpmässigt svar från fallback listan.
        if not found:
            print("Zeta:", random.choice(fallback))

        #Denhär delen gör att programmet kollar efter farewell words i användarens unput och om den hittar något så kommer den avsluta loopen och avsluta programmet.
        if any(word in user_lc for word in farewell_words):
            break

     

if __name__ == "__main__":
    main()

