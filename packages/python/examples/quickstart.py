"""Quickstart — drive a real Chrome session via Ceki from a tool-calling agent.

    CEKI_API_KEY=... OPENAI_API_KEY=... python examples/quickstart.py
"""
import asyncio

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from langchain_ceki import CekiToolkit


async def main() -> None:
    toolkit = CekiToolkit(default_rent={"mode": "incognito"})
    tools = toolkit.get_tools()

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You drive a real Chrome browser via the ceki_* tools. "
                "Always end with ceki_stop.",
            ),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)

    try:
        result = await executor.ainvoke(
            {
                "input": (
                    "Rent a browser (schedule_id 1), navigate to https://example.com, "
                    "take a snapshot, then stop the session and tell me the headline "
                    "you saw."
                ),
            }
        )
        print(result["output"])
    finally:
        await toolkit.aclose()


if __name__ == "__main__":
    asyncio.run(main())
