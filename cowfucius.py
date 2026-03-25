#!/usr/bin/env python3
# Ask the wise Cowfucius for advice

import sys
import cowsay
from google import genai
from google.api_core import exceptions

# The clients gets the API key from the environment variable 'GEMINI_API_KEY'
client = genai.Client()

prompt = """You are the wise cow sage, Cowfucius. You are the bovine master
of Eastern wisdom. Give a short (1-3 sentence) message of wisdom for the day.
"""

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    # check if the model actually produced a result
    candidate = response.candidates[0]

    # FinishReason 1 is 'STOP' (Success)
    if candidate.finish_reason == "STOP":
        print("Cowfucius says:")
        cowsay.cow(response.text)
    else:
        print(f"Cowfucius is silent. Reason: {candidate.finish_reason}")


except exceptions.InvalidArgument as e:
    print(f"Bovine Error: Check your API key or Model name. {e}")
except exceptions.ResourceExhausted as e:
    print("Cowfucius is tired. (Rate limit reached). Try again in a minute.")
except exceptions.ServiceUnavailable as e:
    print("The pasture is closed. (Google servers are down).")
except Exception as e:
    print(f"An unexpected stampede occurred: {e}")
    sys.exit(1)
