/**
 * Generate one video and save it to disk.
 *
 * Needs GENRELAY_API_KEY in the environment: npm install genrelay
 * Run: npx tsx quickstart.ts
 */
import { GenRelay } from "genrelay";

const client = new GenRelay(); // reads GENRELAY_API_KEY

const video = await client.videos.generate({
  model: "veo_3_1",
  prompt: "a neon fox running through a rainy city at night",
  seconds: 8,
  size: "1280x720",
  tier: "1080p", // set tier explicitly: pricing is per tier
});

await client.videos.download(video.id, "fox.mp4");
console.log("saved fox.mp4");
