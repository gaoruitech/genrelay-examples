# AGENTS.md

Guidance for AI coding agents (Cursor, Claude Code, Copilot, Codex) working with GenRelay.

## What GenRelay is

GenRelay is a generative media API: one key and one OpenAI-compatible base URL (`https://genrelay.ai/v1`) for video, image and chat models.

## How to call it

- Video and image generation: use the Python SDK (`pip install genrelay`), the JS/TS SDK (`npm install genrelay`) or the MCP server (`npx -y genrelay-mcp`). Both read `GENRELAY_API_KEY`.
- Chat and image edits: point the official `openai` SDK at `https://genrelay.ai/v1`. See `python/openai_compat.py`.
- Video jobs are asynchronous: submit, poll, download. `client.videos.generate(...)` does all three; `create` + `wait` gives you control.

## Rules that avoid wasted money

- Always set `tier` explicitly (`720p`/`1080p`/`4k` for Veo, `1k`/`2k`/`4k` for images). A `size` that matches no tier falls back to the base rate.
- On a timeout, keep the task id and poll it later. Do not resubmit: a resubmission is billed again.
- Never hard-code API keys. Read `GENRELAY_API_KEY` from the environment.

## Reference

- Docs: https://genrelay.ai/docs
- Pricing: https://genrelay.ai/pricing
- Python SDK: https://github.com/gaoruitech/genrelay-python
- JS/TS SDK: https://github.com/gaoruitech/genrelay-js
- MCP server: https://github.com/gaoruitech/genrelay-mcp
