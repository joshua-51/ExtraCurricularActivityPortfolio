from google import genai

GEMINI_API_KEY = "PRIVATE INFORMATION"
client = genai.Client(api_key=GEMINI_API_KEY)
name = None

def GeminiPromptSynthesis(user_prompt, filename):
    try:
        # Requesting the content
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", 
            contents=f"You are a dino. Make me detailed notes on this topic: {user_prompt}"
        )
        
        # Pulling the text into a variable
        ai_text = response.text

        # WRITING TO FILE
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"TOPIC: {user_prompt}\n")
            file.write("-" * 30 + "\n")
            file.write(ai_text)
        
        # This is the ONLY thing that should print
        print(f"--- Process Complete: Check {filename} ---")
        
        return ai_text

    except Exception as e:
        print(f"Error: {e}")
        return None