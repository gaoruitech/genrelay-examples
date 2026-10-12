"""Use the official OpenAI Python SDK against GenRelay's OpenAI-compatible endpoint.

Chat completions work as usual. Video generation is asynchronous and is not part
of the OpenAI SDK, so use the genrelay package for that (see quickstart.py).
"""
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://genrelay.ai/v1",
    api_key=os.environ["GENRELAY_API_KEY"],
)

resp = client.chat.completions.create(
    model="glm-5.2",
    messages=[{"role": "user", "content": "Write a one-line prompt for a cinematic video of a lighthouse at dusk."}],
)
print(resp.choices[0].message.content)
