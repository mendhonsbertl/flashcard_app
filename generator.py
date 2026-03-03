import os
from client import client
import json





def create_flashcards(topic, level, cards_missing, existing_cards):    #the LLM creates the number of missing flashcard for the next session and checks if it doesn't produce any duplicates
  
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents =  f"""You are a good, strict and benevolent teacher.
        I want you to create {cards_missing} flashcards about {topic}.
        The student is at the {level} level.
        The levels go from 'beginner', 'intermediate', 'advanced' to 'professional'.
        Adjust accordingly
        These cards already exist, do not create questions that cover the same concept even if worded differently:
        {existing_cards}
        Return only a JSON array like this:
        [{{"front": "question here", "back": "answer here", "confidence": 0}}]
        no extra text, no markdown, just raw json."""
    )
    try:
        response_dict = json.loads(response.text)
        return response_dict
    except json.JSONDecodeError:
        print("JSONDecodeerror, somethings wrong with gemini")
        return None

def save_cards(topic, level, cards):        #cards are getting saved to cards.json
    
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as json_file:
            data = json.load(json_file)
    else:
        data = {}
    
    if topic in data:
        if level in data[topic]:
            data[topic][level].extend(cards)
        else:
            data[topic][level] = (cards)
    else:
        data[topic] = {}
        data[topic][level] = cards
    
    with open("cards.json", "w") as f:
        json.dump(data, f, indent=4)

def update_cards(topic, level, cards):               #updates the confidence score of the cards in cards.json
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as f:
            data = json.load(f)
    else:
        raise FileNotFoundError("cards.json not found")
    
    
    updated = {card["front"]: card["confidence"] for card in cards}
    for saved_card in data[topic][level]:
        if saved_card["front"] in updated:
            saved_card["confidence"] = updated[saved_card["front"]]
    
    with open("cards.json", "w") as file:
        json.dump(data, file, indent=4)


