import os
from groq import Groq
from dotenv import load_dotenv

##Load environment variables
load_dotenv()

##Read API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

##Create Groq client
client = Groq(api_key=GROQ_API_KEY)


def ask_llm(prompt):

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content