"""Submit a video job, do other work, then come back for the result.

Video generation takes seconds to minutes. Persist job.id so you can resume
later instead of resubmitting (resubmitting bills a second time).
"""
from genrelay import GenRelay

client = GenRelay()  # reads GENRELAY_API_KEY

job = client.videos.create(model="veo_3_1", prompt="a lighthouse at dusk, 35mm film grain", seconds=8)
print(job.id, job.status)  # task_xxx queued

# ... do other work, store job.id, come back later ...

video = client.videos.wait(
    job.id,
    timeout=900,
    on_progress=lambda v: print(f"{v.status} {v.progress}%"),
)
client.videos.download(video.id, "lighthouse.mp4")
print("saved lighthouse.mp4")
