from normalizer import normalize_topic
from card_filter import get_cards_for_session, load_cards
from generator import create_flashcards, save_cards, update_cards
import random

def change_confidence(card):            #changes the confidence of the loaded cards
    answer = input("Please answer with 1-4: ")
    
    if answer == "1":
        card["confidence"] -= 3
        if card["confidence"] < 1:
            card["confidence"] = 1
    elif answer == "2":
        if card["confidence"] < 5:
            card["confidence"] += 1
        elif card["confidence"] > 5:
            card["confidence"] -= 1
    elif answer == "3":
        if card["confidence"] < 5:
            card["confidence"] += 2
        if card["confidence"] == 5:
            card["confidence"] += 1
    elif answer == "4":
        card["confidence"] += 3
        if card["confidence"] > 9:
            card["confidence"] = 9
    else:
        change_confidence(card)

    
    





def learn_cards(selected_cards, topic, level):      #classic learning through repetition
    if len(selected_cards) == 0:
        return
    studied_cards = []
    session_cards = selected_cards
    while len(session_cards) > 0:
        current_card = session_cards.pop(random.randint(0, len(session_cards)-1))
        print(current_card["front"])
        input("Press Enter to show the answer:")
        print(current_card["back"])
        print("Did you know the answer to this card?")
        print("1: Not at all, 2: Only some parts, 3: Most of it, 4: I know the answer perfectly")
        change_confidence(current_card)
        studied_cards.append(current_card)


    recuring_cards = [card for card in studied_cards if card["confidence"] < 7]     #doesn't recure perfected cards otherwise infinite loop
    update_cards(topic, level, studied_cards)
    learn_cards(recuring_cards, topic, level)



def create_session():                   #creates the session for the classic learning experience

    right_topic = "n"
    user_level = None
    user_time = None
    print("What topic would you like to learn?")

    while right_topic.lower() != "y":
        user_topic = input("Choose your topic (write any subject): ")
        normed_topic = normalize_topic(user_topic)
        print(f"The AI chose '{normed_topic}' for you. Is this what you wanted?")
        right_topic = input("Is this what you wanted?  (y/n)  :")
    
    print(f"Next we need to know how familiar you are with {normed_topic}.")

    while user_level not in ["1", "2", "3", "4"]:
        print("1: BEGINNER")
        print("2: INTERMEDIATE")
        print("3: ADVANCED")
        print("4: PROFESSIONAL")
        print("Please answer with just 1, 2, 3 or 4.")
        user_level = input("Your Answer: ")
    
    level_map = {"1": "beginner","2": "intermediate", "3": "advanced", "4": "professional"}
    actual_level = level_map[user_level]
    
    print("Only one more question before we start.")
    print(f"How much time do you want to spend on {normed_topic}.")

    while user_time not in ["1", "2", "3"]:
        print("1: 15min")
        print("2: 30min")
        print("3: 60min")
        print("Please answer with just 1, 2 or 3.")
        user_time = input("Your Answer: ")

    time_map = {"1": 15, "2": 30, "3": 60}
    actual_time = time_map[user_time]

    return normed_topic, actual_level, actual_time
    
def run_session(normed_topic, actual_level, actual_time):       #runs the created session
    
    loaded_cards = load_cards(normed_topic, actual_level)
    selected_cards, missing_cards = get_cards_for_session(loaded_cards, actual_time)
    print(f"{missing_cards} cards missing")

    while missing_cards > 0:
        card_fronts = [card["front"] for card in loaded_cards]

        created_cards = create_flashcards(normed_topic, actual_level, missing_cards, card_fronts)
        if created_cards == None:
            print("Failed to generate Cards, pleas try again")

        save_cards(normed_topic, actual_level, created_cards)
        loaded_cards = load_cards(normed_topic, actual_level)
        selected_cards, missing_cards = get_cards_for_session(loaded_cards, actual_time)
    
    learn_cards(selected_cards, normed_topic, actual_level)


        
    

    

    




