# AI Research Agent

An autonomous research agent that searches the web, synthesizes information, and generates structured research reports using LangGraph and Claude.

## How It Works

1. Takes a research question as input
2. Uses Tavily to search the web for relevant sources
3. Claude (claude-sonnet-4-5) reasons over the results
4. Returns a structured research report

## Tech Stack

- **LangGraph**: agent loop and orchestration
- **LangChain**: tooling and LLM interface
- **Anthropic Claude**: LLM backbone
- **Tavily**: real-time web search

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

**Query:** What are the latest breakthroughs in AI agents in 2025?

**Output:**

Based on the latest information, here are the key breakthroughs and trends in AI agents in 2025:

## Major Breakthroughs & Developments

### 1. The "Year of the AI Agent"
2025 is widely being called the breakthrough year for AI agents, with industry leaders like Nvidia's Jensen Huang declaring that "the age of agentic AI has arrived." The focus has shifted from standalone large language models (LLMs) to autonomous AI agents that can perform complex tasks independently.

### 2. Massive Venture Funding
AI agent startups attracted approximately $700 million in venture funding in the first half of 2025 alone, indicating massive investor confidence in the technology.

### 3. Evolution to Compound AI Systems
There's been a significant shift from monolithic AI models to compound AI systems. Modern AI agents now integrate with external databases, multiple tools and APIs, and have greater adaptability to different contexts.

## Key Trends for 2025
1. Hyperautomation
2. AI-Powered Decision Intelligence
3. Personalized Employee Experiences
4. Enhanced Customer Interactions
5. AI Orchestrators