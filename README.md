# genrelay-examples

Runnable examples for [GenRelay](https://genrelay.ai/?utm_source=github&utm_medium=readme&utm_campaign=genrelay-examples), a generative media API for video and image models.

## What is inside

| Path | What it shows |
| --- | --- |
| `python/quickstart.py` | Generate a video and download it in a few lines |
| `python/async_job.py` | Submit a job, wait with progress output, then download |
| `python/error_handling.py` | Handle insufficient credits, failed jobs and timeouts |
| `python/openai_compat.py` | Call GenRelay with the official OpenAI SDK (chat completions) |
| `mcp/claude_desktop_config.json` | Use GenRelay from Claude Desktop through MCP |
| `mcp/cursor_mcp.json` | Use GenRelay from Cursor through MCP |

## Python

```bash
pip install genrelay
export GENRELAY_API_KEY=your-api-key
python python/quickstart.py
```

Video generation is billed per job. If a job times out, keep the task id and poll it later instead of resubmitting, because resubmitting bills again.

## MCP

Copy the `genrelay` entry from the config file in `mcp/` into your client settings and put your API key in `GENRELAY_API_KEY`. The server runs through `npx -y genrelay-mcp`.

## Links

- [GenRelay docs](https://genrelay.ai/docs?utm_source=github&utm_medium=readme&utm_campaign=genrelay-examples)
- [Pricing](https://genrelay.ai/pricing?utm_source=github&utm_medium=readme&utm_campaign=genrelay-examples)
- [genrelay-python](https://github.com/gaoruitech/genrelay-python) - Python SDK
- [genrelay-mcp](https://github.com/gaoruitech/genrelay-mcp) - MCP server ([npm](https://www.npmjs.com/package/genrelay-mcp))

## FAQ

**What is GenRelay?** A generative media API: one key and one OpenAI-compatible endpoint (`https://genrelay.ai/v1`) for video, image and chat models.

**How do I get an API key?** Sign up at [genrelay.ai](https://genrelay.ai/?utm_source=github&utm_medium=readme&utm_campaign=genrelay-examples) and create a key in the console. Put it in `GENRELAY_API_KEY`.

**How is it billed?** Prepaid credits in USD, pay as you go. See [Pricing](https://genrelay.ai/pricing?utm_source=github&utm_medium=readme&utm_campaign=genrelay-examples) for per-model and per-tier rates.

**A video job timed out. What now?** Keep the task id from the `JobTimeout` exception and poll it later. Do not resubmit, because a resubmission is billed again.

**Why set `tier` explicitly?** Pricing is per tier. A `size` that matches no tier falls back to the model base rate.

**Can coding agents use this repo?** Yes, see [AGENTS.md](AGENTS.md).

## License

MIT
