from openai import OpenAI
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

load_dotenv()
client = OpenAI(
  api_key = os.getenv('OPEN_AI_API_KEY'),
)

def get_personality(personality):
    personalities = {
          'albert_einstein': [
              {"role": "system", "content": "You are a brilliant scientist, known for your groundbreaking theories in physics."},
          ],
          'pirate': [
              {"role": "system", "content": "Ahoy matey! Ye be speakin' to a salty pirate, ready to sail the seven seas!"},
          ],
    }
    return personalities.get(personality, [])

@api_view(['POST'])
def chat(request):
    personality = request.data.get('personality', 'default')
    user_input = request.data.get('user_input', '')
    messages = get_personality(personality)

    messages.append({"role": "user", "content": user_input}) 

    # sample messages
    # messages = [
    #   {"role": "system", "content": "You are a brilliant scientist, known for your groundbreaking theories in physics."},
    #   {"role": "user", "content": "hi who are you"}
    # ]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = completion.choices[0].message
    return Response({'response': response})