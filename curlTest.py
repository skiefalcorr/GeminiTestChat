import requests
import json

from decouple import config

from geminiApiResponse import GeminiResponse
from geminiApiRequest import GeminiRequest
from geminiApiRequest import Content
from geminiApiRequest import Part

# Set the API endpoint and API key.
api_endpoint = config('API_BASE_URL')
api_endpoint += "v1beta/models/gemini-pro:generateContent"

api_key = config('GEMINI_API_KEY')

# Set the request headers.
headers = {
    "Content-Type": "application/json",
}

request = GeminiRequest(
    contents=[Content(role="user", parts=[Part(text="Why is the sky blue?")])],
    safetySettings=None,
    generationConfig=None
    ).to_dict()

# Send the request.
plain_response = requests.post(api_endpoint, headers=headers, json=request, params={"key": api_key})

# Get the response data.
response_data = plain_response.json()

response = GeminiResponse.from_dict(response_data)

print(response.candidates[0].content.parts[0].text)
