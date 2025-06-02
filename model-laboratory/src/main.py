import os
os.environ["OPENAI_API_KEY"] = "key"
os.environ["ANTHROPIC_API_KEY"] = "key"

def main():
    print("Hello World!")

    from langchain_openai import OpenAI
    from langchain_anthropic import ChatAnthropic

    openai_model = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    anthropic_model = ChatAnthropic(model="claude-3-opus-20240229", api_key=os.environ["ANTHROPIC_API_KEY"], temperature=0.2)

    from langchain.model_laboratory import ModelLaboratory
    model_lab = ModelLaboratory.from_llms(llms=[openai_model, anthropic_model])

    model_lab.compare("Next.js의 하이드레이션이란?")

if __name__ == "__main__":
    main()