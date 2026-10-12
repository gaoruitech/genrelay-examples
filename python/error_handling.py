"""Handle the three outcomes you should plan for: no credits, a failed job, a timeout."""
from genrelay import (
    GenRelay,
    GenRelayError,
    InsufficientCreditsError,
    JobFailedError,
    JobTimeout,
)

client = GenRelay()  # reads GENRELAY_API_KEY

try:
    video = client.videos.generate(model="veo_3_1", prompt="a paper boat on a puddle", tier="720p")
    client.videos.download(video.id, "boat.mp4")
except InsufficientCreditsError:
    print("Out of credits (402): top up, then retry.")
except JobFailedError as e:
    print("The model could not produce a result:", e.video.error)
except JobTimeout as e:
    # Still running. Keep the id and poll later; do not resubmit.
    print("Still running, task id:", e.task_id)
except GenRelayError as e:
    print("GenRelay error:", e)
