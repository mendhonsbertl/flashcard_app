from client import client
import os
import json

def normalize_topic(topic):                 #normalizes topics so there are no duplicate categories because of spelling mistakes or capitalisation
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as f:
            data = json.load(f)
            list_of_keys = list(data.keys())
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""Here is a list of Topics:{list_of_keys}
                            These Topics are used to create flashcards.
                            Here is the new Topic:{topic}.
                            If there are any spelling mistakes in the new Topic correct them.
                            If the new Topic is completely related to ones of the list i gave you, change it to an existing one 
                            If the new topic is different enough to have some similarities to the existing ones
                            use it as your answer. Your answer is only the normalized topic and is 1-3 words long.
                            No other text or anything else."""
            )
            return response.text
    else:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Here is a Topic: {topic}. It is used to create Flashcards.
                        If there are any spelling mistakes in the topic please correct them.
                        You should return the topic in 1-3 words that describe it best.
                        Your answer is only the normalized topic and is 1-3 words long.
                        No other text or anything else."""
        )
        return response.text
    

def normalize_topic_exporter(topic):            #checks the topic for the exporter and makes sure the category exists before exporting
    if os.path.exists("cards.json"):
        with open("cards.json", "r") as f:
            data = json.load(f)
            list_of_keys = list(data.keys())
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""Here is a list of Topics:{list_of_keys}
                            These Topics are used to create flashcards.
                            Here is the new Topic:{topic}.
                            If there are any spelling mistakes in the new Topic correct them.
                            If the new Topic isn't completely related to ones of the list i gave you, reply with 'Topic not found' no other text or anything else. 
                            If the new topic is close enough to have a lot of similarities to one of the existing ones
                            use one of the already existing ones as your answer. Your answer is only the normalized topic and is 1-3 words long.
                            No other text or anything else."""
            )
            if response.text == "Topic not found":
                print(response.text)
                new_topic = input("Please enter an existing topic: ")
                return normalize_topic_exporter(new_topic)
            else:
                return response.text
    else:
        print("There are no cards to export yet")
        return None
        

