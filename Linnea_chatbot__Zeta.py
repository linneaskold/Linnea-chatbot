import random

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
        "Why not, you can tell me about anything!",
        "Why not you can tell me if something is bothering you!"
        ])


]

# fallback answers if keywords not found
fallback = [
    "Tell me more about something you like!",
    "I dont really understand you, explain more so that I can understand!",
    "I dont have knowledge about that, tell me about something else!",
    "Sorry I dont have a answer to that in my program"
]

farewell_words = ["bye", "byee", "goodbye", "see you"]


def run_zeta():
    print("Hello, I am a bot named Zeta. Is there anything you want to talk about today?")
    print("If you no longer wish to talk to me just type bye")


def main():
    run_zeta()

    while True:
        user = input("You: ").strip()
        if not user:
            continue

        user_lc = user.lower()
        found = False

        for keywords, responses in rules:
            if any(word in user_lc for word in keywords):
                answer = random.choice(responses)
                print("bot:", answer)
                found = True
                break

        if not found:
            print("bot:", random.choice(fallback))

        if any(word in user_lc for word in farewell_words):
            break


if __name__ == "__main__":
    main()

