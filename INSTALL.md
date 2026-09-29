# Install the Email Awesome product skill

Install the complete `skills/emailawesome/` folder, including `SKILL.md` and `references/`. Add other folders only when you need their technical recipes. Preserve folder names and relative paths.

## Any LLM or agent harness

1. Register `skills/emailawesome/` as a skill or load its `SKILL.md` when the user asks to use or troubleshoot Email Awesome.
2. Allow the agent to read the skill's own references. Browser/computer use requires a compatible agent and an authenticated product session; the skill does not provide those capabilities itself.
3. If you install a technical recipe too, make it and `emailawesome` available together. Run the ordinary Python 3 helpers only when their specific data-preparation task calls for them.
4. Keep credentials in the product, authenticated connector, secret store or process environment; never add them to prompts, repositories or generated files.

Starter request: `Use Email Awesome to verify this small authorized list, keep every source row, wait for final results, and tell me which addresses need review.`

## Optional Codex or OpenAI adapter

Each `agents/openai.yaml` file provides optional display and starter-prompt metadata. It is not required by the skill logic and can be ignored by Claude, GLM, DeepSeek, custom agents, and other compatible harnesses.

The product skill does not require an MCP server. See [COMPATIBILITY.md](COMPATIBILITY.md) for portability details.
