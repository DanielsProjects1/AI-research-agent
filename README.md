# AI Research Agent

An autonomous research agent that searches the web, synthesizes information, and generates structured research reports using LangGraph and Claude.

## How It Works

1. Takes a research question as input
2. Uses Tavily to search the web for relevant sources
3. Claude (claude-sonnet-4-5) reasons over the results
4. Returns a structured research report

## Tech Stack

- **LangGraph** — agent loop and orchestration
- **LangChain** — tooling and LLM interface
- **Anthropic Claude** — LLM backbone
- **Tavily** — real-time web search

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
ANTHROPIC_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
4. Run the agent:
```bash
   python agent.py
```

## Example Output

Ask any research question and the agent returns a structured report with sourced findings.