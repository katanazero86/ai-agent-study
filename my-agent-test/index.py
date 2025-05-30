# index.py

from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("Hello World")
    print(os.getenv("LANGSMITH_TRACING"))
    print(os.environ["LANGSMITH_PROJECT"])

    # LangChain Hub
    from langchain import hub
    # Hub 에서 ReAct 프롬프트 가져오기
    prompt = hub.pull("hwchase17/react", api_key=os.getenv("LANGSMITH_API_KEY"))

    print(prompt)

    # OpenAI
    from langchain_openai import OpenAI
    # 사용할 LLM
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # SerpAPIWrapper 를 통해 도구 모듈 가져오기
    from langchain_community.utilities import SerpAPIWrapper
    from langchain.tools import Tool

    # SerpAPIWrapper 인스턴스 생성
    search = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

    # 도구 목록 준비
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="LLM이 관련 지식이 없을 때 지식 검색에 사용."
        )
    ]

    # ReAct 에이전트 기능 가져오기
    from langchain.agents import create_react_agent
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    # Agent 실행기 가져오기
    from langchain.agents import AgentExecutor

    # 도구 전달
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 호출
    print("첫 번째 실행 결과:")
    agent_executor.invoke(
        {
            "input": "현재 인공지능 에이전트의 최신 연구 동향은 무엇입니까?"
        }
    )
    print("두 번째 실행 결과:")
    agent_executor.invoke(
        {
            "input": "현재 인공지능 에이전트의 최신 연구 동향은 무엇입니까?"
        }
    )


if __name__ == "__main__":
    main()
