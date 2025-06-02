import os

os.environ[
    "OPENAI_API_KEY"] = "key"


def main():
    print("Hello World!")

    # 출력을 문자열로 변환하기 위한 출력 분석기
    from langchain_core.output_parsers import StrOutputParser
    # 대화 프롬프트 템플릿을 생성하기 위한 모듈
    from langchain_core.prompts import ChatPromptTemplate
    # OpenAI GPT 모델을 호출하기 위한 모듈
    from langchain_openai import ChatOpenAI

    prompt = ChatPromptTemplate.from_template("{topic}에 대한 이야기를 들려주세요.")

    model = ChatOpenAI(model="gpt-3.5-turbo")

    output_parser = StrOutputParser()

    # 파이프라인 연산자를 사용하여 각 처리 단계를 연결해 하나의 처리 구조로 연동
    chain = prompt | model | output_parser

    message = chain.invoke({"topic": "리액트"})

    print(message)


if __name__ == "__main__":
    main()
