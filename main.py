import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()

# load API
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

# user input
    verbose = '--verbose' in sys.argv
    user_prompt = " ".join(arg for arg in sys.argv[1:] if arg != "--verbose")   

# system prompt missing error handling
    if not user_prompt.strip():
        print("Missing prompt!")
        sys.exit(1)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    iteration = 0
    while iteration <= 20:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            )
        )
        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls and len(response.function_calls) >= 1:
            for call in response.function_calls:
                function_call_result = call_function(call, verbose=verbose)
                if verbose:
                    response_data = getattr(
                        function_call_result.parts[0].function_response, "response", None
                    )
                    if response_data is not None:
                        print(f"-> {response_data}")
                    else:
                        raise Exception("Function did not return a valid response.")
                messages.append(function_call_result)
        else:
            print(response.text)
            break

        iteration += 1
main()