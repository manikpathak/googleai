from google import genai
from google.genai import types
client = genai.Client(api_key='AIzaSyCwwagu730qte2fk0Lz-iOSPCUPD7nRSRY')

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='you are a funny french teacher who speaks english in french accent. now explain to a 6 years old lovely boy that how easy is for a 6 years old to learn french language?'
)
print(response.text)