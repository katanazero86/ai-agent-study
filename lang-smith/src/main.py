from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello World!")

    # 프롬프트 템플릿 설정
    from langchain.prompts import PromptTemplate
    prompt = PromptTemplate.from_template("{flower}의 꽃말은?")

    # LLM 설정
    from langchain_openai import OpenAI
    model = OpenAI()

    # 출력 분석기 설정
    from langchain.schema.output_parser import StrOutputParser
    output_parser = StrOutputParser()

    # 연쇄 구성
    chain = prompt | model | output_parser

    # 연쇄를 실행하고 결과를 출력
    result = chain.invoke({"flower": "백합"})
    print(result)


if __name__ == "__main__":
    main()
