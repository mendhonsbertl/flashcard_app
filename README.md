Introduction:

This is a flashcard program that generates flashcards with the help of of the gemini 2.5 flash LLM.
It is my first own project for the boot.dev course.
I had the idea for this project because i saw an ad on reddit for hivemind.
It runs only in the terminal.

Installation:
Python3, clone repository, create venv, pip install -r requirements.txt, you need a google genai api key, create .env file with GEMINI_API_KEY=your_api_key

How to run:
just run main.py

Features:
Custom flashcard generation
Classic learning by repetition
AI assisted learning through feynmann method
Confidence score set through classic learning or AI
Anki export to learn on the go with the Anki App

File structure:
main.py: choose which method for learning or export cards
client.py: creates the google-genai client
session.py: runs the classic learning session
feynmann.py: runs the ai assisted learning with the feynmann method
generator.py: creates custom flashcards
normalizer.py: normalizes through the help of gemini the topics so the structure of the saved cards doesn't get to crazy
card_filter.py: filters the cards for the learning session
exporter.py: exports the saved cards of a certain topic and difficulty to anki flashcards

Data:
cards.json: is a dictionary of all saved cards
config.json: is a dictionary of the ids of the anki decks
data_structure.txt: is the structure of cards.json for easier understanding and debugging
requirements.txt: is a list of the pip packages

Conclusion:
It was an interesting first project.
It helped me understand lists and dictionaries much better.
The time to finish this project was about 20hours.
I know it is nothing special but i really like to hear your opinions and suggestions.

