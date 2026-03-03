import dotenv
import os
from google import genai

dotenv.load_dotenv()
                                            #creates the genai client
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)