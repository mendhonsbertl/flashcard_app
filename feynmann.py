from client import client
from card_filter import load_cards
from generator import create_flashcards, save_cards, update_cards
import random

def feynmann_method(topic, level, time):         #creates a 3 question long conversation with the LLM and you get an evaluation of how you did after each flashcard
    loaded_cards = load_cards(topic, level)
    random_cards = []
    if len(loaded_cards) < time:
        missing_cards = time - len(loaded_cards)
        existing_cards = [card["front"] for card in loaded_cards]
        created_cards = create_flashcards(topic, level, missing_cards, existing_cards)
        save_cards(topic, level, created_cards)
    loaded_cards = load_cards(topic, level)

    random_cards = random.sample(loaded_cards, k=time)

    while len(random_cards) > 0:
        current_card = random_cards.pop(random.randint(0, len(random_cards)-1))
        chat = client.chats.create(model="gemini-2.5-flash")
        response = chat.send_message(f"""You are a benevolent Teacher and are testing a student.
                                    This is the Question from the flashcard: {current_card["front"]} and this is the correct answer from the flashcard: {current_card["back"]}
                                    Test the student on this Flashcard.
                                    The next 3 Replies will be from the student, so you can try to help him with 2 leading questions,
                                    after the first one, but don't make it too obvious.
                                    After the 3rd Question give an overall evaluation of what the students knowledge to the ask question is.
                                    Do this addressing the student directly and limit your answer to 5 sentences max.
                                    Reply to this message only with the first Question to the student, no greetings or anything else.
                                    """)
        i = 0
        while i < 3:
            print(response.text)
            response = chat.send_message(input("Type your answer: "))
            i += 1
        print(response.text)
        score = chat.send_message("""You have to give the student now a score from 1-9.
                                     1 is the student did not know anything about the subject asked
                                     and 9 the student knew the answer to the question perfectly.
                                     Reply with only the score and nothing else""")
        print(score.text)       #only single digit parsing
        try:
            current_card["confidence"] = int(score.text.strip())
        except ValueError:
            print("Could not parse score, keeping original confidence")
        update_cards(topic, level, [current_card])
        


