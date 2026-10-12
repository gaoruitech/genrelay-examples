"""Generate one video and save it to disk.

Needs GENRELAY_API_KEY in the environment: pip install genrelay
"""
from genrelay import GenRelay

client = GenRelay()  # reads GENRELAY_API_KEY

video = client.videos.generate(
    model="veo_3_1",
    prompt="a neon fox running through a rainy city at night",
    seconds=8,
    size="1280x720",
    tier="1080p",  # set tier explicitly: pricing is per tier
)

client.videos.download(video.id, "fox.mp4")
print("saved fox.mp4")
