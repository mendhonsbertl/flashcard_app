Data structure:

Dictionary of a single card:
{
    "front": "What is a pointer?",
    "back": "A variable that stores a memory address",
    "confidence": 3
}
List of dictionaries "cards":

[
    {"front": "...", "back": "...", "confidence": 0},
    {"front": "...", "back": "...", "confidence": 7},
    {"front": "...", "back": "...", "confidence": 3},
]

cards.json:

{
    "C pointers": {
        "beginner": [
            {"front": "...", "back": "...", "confidence": 0},
            {"front": "...", "back": "...", "confidence": 7}
        ],
        "advanced": [
            {"front": "...", "back": "...", "confidence": 3}
        ]
    },
    "ESP32": {
        "beginner": [
            {"front": "...", "back": "...", "confidence": 5}
        ]
    }
}