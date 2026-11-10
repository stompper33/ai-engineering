---
title: deep_research
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

# Deep Research

Deep Research is a **multi-agent AI research assistant** with a web interface. You type a research question, and the app:

1. Asks you a few **clarifying questions** so it understands what you want,
2. **Plans** a set of web searches,
3. Runs those searches **at the same time** and summarizes each one,
4. **Writes** a long, structured Markdown report (1000+ words),
5. Shows the report in the browser and **emails** it to you.

Each step is handled by its own specialized AI agent, built with the **OpenAI Agents SDK**. A single `ResearchManager` coordinates the agents, and the UI is built with **Gradio**.

---

## How it works

```
 User question
      │
      ▼
┌──────────────────────┐   3 follow-up questions shown in the UI
│ Clarification Agent  │ ──────────────────────────────────────────►  User answers (optional)
└──────────────────────┘                                                    │
      ┌─────────────────────────────────────────────────────────────────────┘
      ▼
 Query + answers combined (ResearchManager.build_query)
      │
      ▼
┌──────────────────────┐
│    Planner Agent     │  → WebSearchPlan: N search terms, each with a reason
└──────────────────────┘
      │
      ▼   (asyncio.gather: all searches run in parallel)
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Search Agent │ │ Search Agent │ │ Search Agent │ ...  → short summaries (<300 words each)
└──────────────┘ └──────────────┘ └──────────────┘
      │
      ▼
┌──────────────────────┐
│     Writer Agent     │  → ReportData: summary, full Markdown report, follow-up topics
└──────────────────────┘
      │
      ▼
┌──────────────────────┐
│     Email Agent      │  → HTML email via SMTP (or Pushover notification)
└──────────────────────┘
      │
      ▼
 Report displayed in the Gradio UI
```

### Step by step

1. **Clarification Agent** (`clarification_agent.py`)
   Reads your question and returns a list of clarifying questions as a `Clarifications` Pydantic model. The UI shows one answer box per question. You can answer any or none of them; blank answers are skipped.

2. **Query building** (`ResearchManager.build_query` in `research_manager.py`)
   Adds your question/answer pairs to the original query, so later agents get the full context.

3. **Planner Agent** (`planner_agent.py`)
   Turns the query into a `WebSearchPlan`: a list of `WebSearchItem`s, each with a search `query` and a `reason` for why it matters. The number of searches is set by `HOW_MANY_SEARCHES`.

4. **Search Agent** (`search_agent.py`)
   Uses OpenAI's hosted `WebSearchTool` (with `tool_choice="required"`, so it always searches) and returns a short 2–3 paragraph summary. The manager runs one Search Agent per planned search, **all in parallel** using `asyncio.gather`.

5. **Writer Agent** (`writer_agent.py`)
   Combines all the summaries into a long Markdown report. It returns a `ReportData` model with a `short_summary`, the `markdown_report`, and `follow_up_questions` for further research.

6. **Email Agent** (`email_agent.py`)
   Turns the report into a clean HTML email with a subject line and sends it through the `send_email_tool` function tool. That tool calls `messenger.py`, which sends either:
   - an **email over SMTP** (port 587, STARTTLS), or
   - a **Pushover push notification**, if `USE_EMAIL=false`.

While all this runs, `ResearchManager.run` is an **async generator**: it sends status updates ("Searches planned…", "Writing report…") to the UI as they happen, including a link to the run's **OpenAI trace** so you can inspect every agent call.

---

## Project structure

| File | Purpose |
|------|---------|
| `app.py` | Main Gradio app. Two-step flow: get clarifying questions, then run the research. |
| `simple.py` | Minimal Gradio app with one step (no clarification). |
| `research_manager.py` | `ResearchManager` class that runs the agents in order and streams status updates. |
| `clarification_agent.py` | Agent that writes clarifying questions about the user's query. |
| `planner_agent.py` | Agent that plans the list of web searches. |
| `search_agent.py` | Agent that runs one web search and summarizes the results. |
| `writer_agent.py` | Agent that writes the final Markdown report. |
| `email_agent.py` | Agent and function tool that format and send the report. |
| `messenger.py` | Helpers for SMTP email and Pushover notifications. |
| `styles.py` | Custom dark-theme CSS, autofocus JavaScript, header HTML, and example prompts for the UI. |
| `requirements.txt` | Python dependencies. |

---

## Languages & tech stack

**Languages**
- **Python 3.12**: all application logic
- **CSS / HTML / JavaScript**: custom UI styling and behavior, stored as strings in `styles.py`

**Frameworks & libraries**

| Area | Technology |
|------|------------|
| Agent framework | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) (`openai-agents`): `Agent`, `Runner`, `trace`, `function_tool`, `WebSearchTool`, `ModelSettings` |
| LLM provider | OpenAI API (default model `gpt-5.4-mini`, configurable) |
| Web search | OpenAI hosted `WebSearchTool` |
| Structured outputs | Pydantic models (`Clarifications`, `WebSearchPlan`, `ReportData`) |
| Web UI | Gradio (`Blocks`, `State`, `Examples`, streaming outputs) |
| Concurrency | Python `asyncio` (parallel searches, async streaming) |
| Email | Python standard library `smtplib` + `email.message` |
| Push notifications | Pushover API via `requests` |
| Configuration | `python-dotenv` (`.env` file) |
| Observability | OpenAI Traces dashboard |
| Deployment | Hugging Face Spaces (Gradio SDK, see the frontmatter above) |

---

## Configuration

Create a `.env` file in this folder (or set these as Space secrets on Hugging Face):

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` | Yes | – | Your OpenAI API key |
| `DEFAULT_MODEL_NAME` | No | `gpt-5.4-mini` | Model used by every agent |
| `HOW_MANY_SEARCHES` | No | `5` | Number of web searches the planner creates |
| `CLARIFICATION_QUESTIONS` | No | `3` | Number of clarifying questions to ask |
| `USE_EMAIL` | No | `true` | `true` = send email over SMTP; `false` = send a Pushover notification instead |
| `EMAIL_ADDRESS` | If email | – | Sender **and** recipient address |
| `EMAIL_SMTP_SERVER` | If email | – | SMTP host (e.g. `smtp.gmail.com`, port 587) |
| `EMAIL_APP_PASSWORD` | If email | – | App password for the email account |
| `PUSHOVER_USER` | If Pushover | – | Pushover user key |
| `PUSHOVER_TOKEN` | If Pushover | – | Pushover app token |

Note: See example file `.evn.example` for reference
---

## Running locally

```bash
cd deep_research
pip install -r requirements.txt     # or: uv pip install -r requirements.txt
# create your .env file (see Configuration)
python app.py                        # full app with clarifying questions
# or
python simple.py                     # minimal version
```

Then open the local URL Gradio prints (usually http://127.0.0.1:7860), type a question or pick an example, press **Investigate**, answer any clarifying questions, and press **Start research**.

---

## Notes

- The report is emailed to **your own** `EMAIL_ADDRESS` (it is both sender and recipient).
- Each run makes several OpenAI calls, including paid web searches, so more searches means higher cost.
- Every run creates an OpenAI trace (the link appears in the UI), which is useful for debugging and for seeing what each agent did.
