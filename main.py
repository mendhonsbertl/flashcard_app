
from session import run_session, create_session
from feynmann import feynmann_method
from normalizer import normalize_topic_exporter
from exporter import export_cards_to_anki, find_level

def main():
    
    print("Hello to the Flashcard Program")
    while True:
        user_input = 0
        while user_input not in ["1", "2", "3", "4"]:
            print("What do you want to do?")
            print("1: Learn with flashcards")
            print("2: Learn with AI Assistance")
            print("3: Export flashcards to Anki")
            print("4: QUIT")
            user_input = input("What do you want to do: ")

        
        if user_input == "1":
            print("You've chosen to learn with flashcards")
            normed_topic, actual_level, actual_time = create_session()
            print("The program will now find or create flashcards for your session")
            run_session(normed_topic, actual_level, actual_time)
            
        elif user_input == "2":
            print("You've chosen learning with AI. The AI will ask you questions and evaluate your answers.")
            normed_topic, actual_level, actual_time = create_session()
            feynmann_method(normed_topic, actual_level, actual_time)
            

        elif user_input == "3":
            print("You've chosen to export flashcards")
            topic_answer = 0
            while topic_answer != "y":
                exporter_topic = input("Please enter an existing topic: ")
                normalized_exporter_topic = normalize_topic_exporter(exporter_topic)
                print(f"{normalized_exporter_topic} is this the topic you wanted?")
                topic_answer = input("(y/n):" ).lower().strip()
            found_level = find_level(normalized_exporter_topic)
            export_cards_to_anki(normalized_exporter_topic, found_level)
            print("Export finished")
            
        elif user_input == "4":
            quit_answer = 0
            while quit_answer not in ["y", "n"]:
                quit_answer = input("Do you really want to quit(y/n): ").lower()
            
                if quit_answer == "y":
                    return
                

main()



    

