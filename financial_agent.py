from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

IntelliAgents=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# IntelliAgents.print_response("Summarize analyst recommendations, stock_fundamentals and share latest news for Tesla & get me latest updates about tesla from the web",stream=True)
IntelliAgents.print_response("Summarize analyst recommendations and share latest news for Tesla",stream=True)

