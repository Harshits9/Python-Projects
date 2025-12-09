import google.generativeai as genai
import os
import sys

# ---------------------------------------------------------------------------
# SETUP
# 1. Get your free API Key here: https://aistudio.google.com/app/apikey
# 2. Paste it inside the quotes below.
# ---------------------------------------------------------------------------
GOOGLE_API_KEY = ""

# Configure the library
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    print(f"Error configuring API: {e}")

# Initialize the model
# We use 'gemini-1.5-flash' because it is fast and free.
# If you get a 404 error, RUN: pip install --upgrade google-generativeai
model = genai.GenerativeModel('gemini-1.5-flash')

# Start the chat history
chat_session = model.start_chat(history=[])

def completion(user_message):
    try:
        # Send message to Gemini
        response = chat_session.send_message(user_message)
        
        # Print response
        print(f"Jarvis: {response.text}")
        
    except Exception as e:
        # Detailed error handling
        print(f"\nJarvis: I encountered an error: {e}")
        if "404" in str(e) and "not found" in str(e).lower():
            print("\n[TIP]: This error usually means your google library is old.")
            print("       Please run: pip install --upgrade google-generativeai")

if __name__ == "__main__":
    print("---------------------------------------------------------")
    print("Jarvis (Gemini Powered) is ready!")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("---------------------------------------------------------\n")
    print("Jarvis: Hello! How may I help you today?\n")
    
    while True:
        try:
            # Get user input
            user_question = input("User: ")
            
            # Check for exit keywords
            if user_question.lower() in ['exit', 'quit']:
                print("Jarvis: Goodbye!")
                break
            
            # Skip empty inputs
            if not user_question.strip():
                continue
                
            # Get response
            completion(user_question)
            
        except KeyboardInterrupt:
            print("\nJarvis: Goodbye!")
            break
        except Exception as e:

            print(f"An unexpected error occurred: {e}")
