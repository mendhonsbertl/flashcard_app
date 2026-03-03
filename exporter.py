import genanki
import os
import json
import random

def export_cards_to_anki(topic, level):                 #exports existing flashcard to the .apkg format
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as f:
            data = json.load(f)
    else:
        raise FileNotFoundError("cards.json not found")
    
    if topic in data:
        if level in data[topic]:
            print("Cards found")
        else:
            print("Cards not found")
            return
    else:
        print("Cards not found")
        return
    
    model_id = random.randrange(1 << 30, 1 << 31)       #creates large random id
    deck_id = random.randrange(1 << 30, 1 << 31)
    saved_ids = {}
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            saved_ids = json.load(f)
        if topic in saved_ids:
            if level in saved_ids[topic]:
                model_id = saved_ids[topic][level]["model_id"]
                deck_id = saved_ids[topic][level]["deck_id"]
            else:
                saved_ids[topic][level] = {"model_id": model_id, "deck_id": deck_id}

        else:
            saved_ids[topic] = {}
            saved_ids[topic][level] = {"model_id": model_id, "deck_id": deck_id}
    else:
        saved_ids[topic] = {}
        saved_ids[topic][level] = {"model_id": model_id, "deck_id": deck_id}

    

    with open("config.json", "w") as f:
        json.dump(saved_ids, f, indent= 4)

    my_model = genanki.Model(
        model_id,
        "Simple Model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                 "name": "Card1",
                 "qfmt": "{{Question}}",
                 "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
            
        ]
    )
    
    my_deck = genanki.Deck(
        deck_id,
        f"{topic}, Level = {level}"
    )

    cards = data[topic][level]

    for card in cards:
        current_note = genanki.Note(
            model=my_model,
            fields=[card["front"], card["back"]]
        )

        my_deck.add_note(current_note)
    
    os.makedirs("exports", exist_ok=True)
    genanki.Package(my_deck).write_to_file(f"exports/{topic}_{level}.apkg")
  
def find_level(topic):                  #standardizes the level so inputs don't break main
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as f:
            data = json.load(f)
    else:
        print("cards.json doesn't exist yet")
        return
    level = 0
    while level not in ["1", "2", "3", "4"]: 
        print("Please chose a level:")
        print("1: BEGINNER")
        print("2: INTERMEDIATE")
        print("3: ADVANCED")
        print("4: PROFESSIONAL")
        level = input("Enter now: ")
    level_map = {"1": "beginner", "2": "intermediate", "3": "advanced", "4": "professional"}
    actual_level = level_map[level]

    if actual_level in data[topic]:
        return actual_level
    else:
        print("level not found")
        return find_level(topic)
    
