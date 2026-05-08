from google import genai

# 1. Your API key from AI Studio
GEMINI_API_KEY = "AIzaSyC6MLOv3rJ9Md7kd4dFiuhkEspc1sXCc6c"

client = genai.Client(api_key=GEMINI_API_KEY)

print("--- Gemini 2026 Free-Tier Test ---")
user_prompt = input("Prompt: ")

try:
    # 2. We are using 'gemini-2.5-flash-lite' because 2.0 is often 'Limit 0'
    # If this fails, try: "gemini-3-flash-preview"
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", 
        contents=user_prompt
    )
    
    print("\nGemini Response:")
    print("-" * 30)
    print(response.text)
    print("-" * 30)

except Exception as e:
    print(f"\n[!] Error: {e}")
    print("\nHELP: If you still see 'limit: 0', go to Google AI Studio,")
    print("click 'Settings' -> 'Plan' and check if 'Free Tier' is toggled ON.")