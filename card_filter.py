import os
import json
import random

def load_cards(topic, level):          #loads cards from the cards.json file
    
    try:
        with open("cards.json", "r") as f:
            data = json.load(f)
            return data[topic][level]   #returns only a list of the relevant cards and not the whole dictionary
    except (FileNotFoundError, KeyError):
        return []                       #returns an empty list that session.py and feynmann.py can handle

def separate_cards(cards):              #separates cards by confidence score
    new_cards = []
    unfamiliar_cards = []
    familiar_cards = []
    perfected_cards = []
    for card in cards:
        if card["confidence"] == 0:
            new_cards.append(card)
        if card["confidence"] != 0 and card["confidence"] < 4:
            unfamiliar_cards.append(card)
        if card["confidence"] > 3 and card["confidence"] < 7:
            familiar_cards.append(card)
        if card["confidence"] > 6:
            perfected_cards.append(card)
    return new_cards, unfamiliar_cards, familiar_cards, perfected_cards


def get_cards_for_session(cards, time):         #puts cards in buckets and makes sure that there are cards from every bucket for the session
    new_cards, unfamiliar_cards, familiar_cards, perfected_cards = separate_cards(cards)
    
    selected_cards = []
    number_perfected_cards = time // 6
    number_familiar_cards = time // 5
    number_unfamiliar_cards = time // 3
    number_new_cards = time - (number_perfected_cards + number_familiar_cards + number_unfamiliar_cards)

    

    while len(perfected_cards) > 0 and number_perfected_cards > 0:
        selected_cards.append(perfected_cards.pop(random.randint(0, len(perfected_cards)-1)))
        number_perfected_cards -= 1
    
    while len(familiar_cards) > 0 and number_familiar_cards > 0:
        selected_cards.append(familiar_cards.pop(random.randint(0, len(familiar_cards)-1)))
        number_familiar_cards -= 1
    
    while len(unfamiliar_cards) > 0 and number_unfamiliar_cards > 0:
        selected_cards.append(unfamiliar_cards.pop(random.randint(0, len(unfamiliar_cards)-1)))
        number_unfamiliar_cards -= 1

    while len(new_cards) > 0 and number_new_cards > 0:
        selected_cards.append(new_cards.pop(random.randint(0, len(new_cards)-1)))
        number_new_cards -= 1
    
    missing_cards = time - len(selected_cards)

    while missing_cards > 0:
        if len(new_cards) > 0:
            selected_cards.append(new_cards.pop(random.randint(0, len(new_cards)-1)))
            missing_cards -= 1
        elif len(unfamiliar_cards) > 0:
            selected_cards.append(unfamiliar_cards.pop(random.randint(0, len(unfamiliar_cards)-1)))
            missing_cards -= 1
        elif len(familiar_cards) >  0:
            selected_cards.append(familiar_cards.pop(random.randint(0, len(familiar_cards)-1)))
            missing_cards -= 1
        else:
            break

   


    return selected_cards, missing_cards

    