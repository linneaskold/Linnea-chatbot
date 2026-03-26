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


#denhär delen av koden är keywords som programmet kommer att leta efter i användarens input för att sen kunna svar på hur mycket klocka eller datumet.
time_keywords = ["time", "what time", "clock"]
date_keywords = ["date", "what date", "day"]
time_and_date_keywords = ["time and date", "date and time", "what time and date"]





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
           "and thats great to hear! What makes you feel that way?",
           "thats wonderful! What makes you feel that way?",
           "thats fantastic! What makes you feel that way?",
           "thats amazing! What makes you feel that way?",
           "thats good to hear! What makes you feel that way?"
            ]),

      # sad
       (["sad", "bad", "terrible", "awful", "depressed"], [
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
        "Why not you can tell me if something is bothering you!"
        ]),

    #yes
    (["yes", "yeah", "yea", "yess", "yup", "absolutely"], [
        "So you really are that sure huh",
        "Its nice that you are so sure about that!",
        "You seem really sure, are you really really sure?",
        "You seem very positive about being sure, tell me more!"
        ]),

    #other response
    (["sure", "good", "okay"], [
        "Then tell me more, im really interested!",
        "Tell me what you really think about that!"
        ]),

    #unsure response
    (["maybe", "perhaps"], [
        "You seem unsure, tell me more so that i can understand better!",
        "If you feel unsure about it yoy can explain it to me so i maybe can help you!"
    ]),

    #the program
    (["bot", "zeta", "you"], [
        "I am as I told you before a bot named Zeta, but lets talk about you, tell me something!",
        "I am a bot named Zeta as you probably alredy know. Now tell me about something you like!",
        "As you know I am a bot named Zeta and did you know that my name is an greek letter! Now tell me something about you!",
        "Did you know that my name Zeta, is the sixth letter of the greek alphabet? Now tell me something about you!"
        ]),

    #school
        (["school", "homework", "class"], [
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
        (["fun", "funny", "enjoyable", "thrilling", "hilarious"], [
            "That sounds fun, tell me more about it!",
            "That sounds really fun, tell me more about it!",
            "That sounds hilarious, tell me more about it!",
            "Tell me more about what makes it so fun!",
            "Tell me more about fun stuff like that!"
            ]),

         #sports
        (["sports", "football", "soccer", "basketball", "golf", "swimming", "tennis"], [
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


  



]



#Här under är fallbacksvar som programmet kommer att använda ifall det inte hittar några keywords i användarens input.

# fallback answers if keywords not found
fallback = [
    "Tell me more about something you like!",
    "I dont really understand you, explain more so that I can understand!",
    "I dont have knowledge about that, tell me about something else!",
    "Sorry I dont have a answer to that in my program"
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

