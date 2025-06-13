import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types


def main():
    load_dotenv()

# load API
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

# user input 
    user_prompt = " ".join(arg for arg in sys.argv[1:] if arg != "--verbose")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]   

# system prompt missing error handling
    if not user_prompt.strip():
        print("Missing prompt!")
        sys.exit(1)

# model response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages,
    )
    
# general printed outupt
    print(response.text)

# verbose tag handling
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

main()