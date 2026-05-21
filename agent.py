from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatAnthropic(model="claude-sonnet-4-5")
tools = [TavilySearch(max_results=3)]
agent = create_react_agent(llm, tools)

def run_agent(question: str):
    print(f"\nResearching: {question}\n")
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    final = result["messages"][-1].content
    print("Research complete. Final results:")
    print(final)
    return final

if __name__ == "__main__":
    run_agent("What are the latest breakthroughs in AI agents in 2025?")