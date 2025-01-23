# IntelliAgents Financial Analyst

## Overview

The **IntelliAgents Financial Analyst** is a powerful and flexible Multi Agent interaction framework designed to combine the capabilities of multiple specialized AI agents to perform complex tasks seamlessly. The system leverages advanced AI models and integrates cutting-edge tools to provide insights, gather information, and process financial data effectively. This project demonstrates the application of AI in web search and financial data analysis through a collaborative agent-based architecture.

## Features

### Web Search Agent
- **Name**: Web Search Agent  
- **Role**: Gathers information from the web.  
- **Model**: `Groq (llama-3.3-70b-versatile)`  
- **Tools Used**: [DuckDuckGo](https://duckduckgo.com/)  
- **Instructions**:
  - Includes sources in all responses.
  - Displays output in Markdown format.
- **Use Case**: Finds the latest updates and information about specific topics from the web.

### Finance AI Agent
- **Name**: Finance AI Agent  
- **Role**: Processes and analyzes financial data.  
- **Model**: `Groq (llama-3.3-70b-versatile)`  
- **Tools Used**: YFinanceTools
  - Stock Prices
  - Analyst Recommendations
  - Stock Fundamentals
  - Company News
- **Instructions**:
  - Presents data in tabular format.
  - Uses Markdown for enhanced readability.
- **Use Case**: Summarizes analyst recommendations, displays stock fundamentals, and fetches the latest company news.

### Multi-Agent Collaboration
- **Name**: IntelliAgents Collaborator  
- **Role**: Coordinates between Web Search Agent and Finance AI Agent to perform tasks requiring both web search and financial analysis.
- **Model**: `Groq (llama-3.3-70b-versatile)`  
- **Instructions**:
  - Always includes sources.
  - Uses tables for financial data presentation.
  - Displays output in Markdown format.
- **Use Case**: Combines web-based insights with financial data to provide a comprehensive view of topics like stock analysis and company performance.

## Accomplishments
1. **Multi-Agent Integration**: Seamlessly integrated multiple AI agents with distinct roles to handle diverse tasks collaboratively.
2. **Web Search Capability**: Implemented a web search agent using DuckDuckGo to fetch real-time, source-backed information.
3. **Financial Data Analysis**: Enabled the analysis and presentation of financial data using YFinanceTools for stock prices, fundamentals, and recommendations.
4. **Advanced AI Model Usage**: Leveraged the `Groq llama-3.3-70b-versatile` model for versatile and accurate outputs.
5. **User-Friendly Outputs**: Ensured outputs are well-structured using Markdown and tabular formats for easy interpretation.

## Technologies Used
- **Programming Language**: Python
- **AI Model**: `Groq llama-3.3-70b-versatile`
- **Libraries and Tools**:
  - [phidata](https://www.phidata.com/): An open-source platform to build, ship and monitor agentic systems.


## How It Works
1. **Web Search Agent**: Fetches the latest information about specific topics from the web, including sources for credibility.
2. **Finance AI Agent**: Summarizes analyst recommendations, displays stock fundamentals, and fetches company news, presenting the output in a structured table.
3. **Multi-Agent Collaboration**: The IntelliAgents Collaborator coordinates between the two agents to deliver comprehensive and integrated responses for complex queries.

## Example Use Case
```python
IntelliAgents.print_response(
    "Summarize analyst recommendations and share latest news for Microsoft",
    stream=True
)
```

**Output**: Combines real-time financial data and web-based insights about Tesla, presenting the results in a user-friendly format.

## Setup and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/saileshdwivedy30/intelliagents-financial-analyst.git
   cd intelliagents-financial-analyst
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your phidata and groq API keys:
4. Run the project:
   ```bash
   python financial_agent.py
   ```
