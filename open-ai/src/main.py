import os


def main():
    print("Hello World")
    os.environ[
        "OPENAI_API_KEY"] = "your-key"

    from openai import OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={
            "type": "json_object"
        },
        messages=[
            {
                "role": "system",
                "content": "당신은 꽃에 대한 전문가야. 지금부터 사용자가 꽃에 대한 질문을 하면 너는 이를 이해하도록 답변을 해주면 된다. 출력 형식은 JSON 형식이야."
            },
            {
                "role": "user",
                "content": "생일 선물로 어떤 꽃이 가장 좋을까요?"
            },
            {
                "role": "assistant",
                "content": "장미꽃은 생일 선물로 인기 있는 선택입니다."
            },
            {
                "role": "user",
                "content": "배송에는 얼마나 걸릴까요?",
            }
        ]
    )

    print(response)
    print(response.choices[0].message.content)


if __name__ == '__main__':
    main()
