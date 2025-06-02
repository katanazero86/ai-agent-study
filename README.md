# ai-agent-study

---

- my-agent-test

ReAct 기반 체계를 이용한 간단한 에이전트   
LangChain + OpenAI + SerpAPI

- OpenAI API 예제

간단한 대화 구현   
간단한 이미지 생성   
각 모델별 토큰 비용 확인 + temperature 주의(너무 높으면 답변 일관성이 없고 정확성이 떨어짐)

- model-laboratory

LangChain을 사용하여 OpenAI와 Anthropic(Claude)의 언어 모델에게 같은 질문을 던지고, 두 모델의 응답을 비교하는 실험을 수행하는 예제

- langchain-chain

LangChain을 사용하여 OpenAI의 GPT 모델에게 "리액트에 대한 이야기를 들려주세요."라는 요청을 보내고, 그 응답을 출력하는 예제   
LangChain Expression Language (LCEL)은 LangChain 체인을 간단하고 선언적으로 연결할 수 있도록 설계된 표현식 문법입니다.
파이프라인 방식으로 여러 컴포넌트를 연결할 수 있어, 마치 함수형 프로그래밍처럼 명확하고 직관적으로 체인을 구성할 수 있습니다.   
```
chain = prompt | model | output_parser
```

- lang-smith

랭스미스(+LangChain)를 사용하여 OpenAI의 GPT 모델에게 질문을 보내고 그 응답을 출력하는 예제   
랭스미스 콘솔을 열어보면, LLM 체인 추적 및 디버깅이 가능

.env
```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="key"
LANGSMITH_PROJECT="프로젝트명"
OPENAI_API_KEY="key"
```

- langchain-node

LangChain과 OpenAI의 LLM(ChatOpenAI)을 사용해 프롬프트 기반 자연어 처리를 수행하고, 실행 과정을 LangSmith의 트레이서(LangChainTracer)를 통해 추적하는 예시   
```
// 체인 구(프롬프트 → LLM → 파서)
const chain = prompt.pipe(llm).pipe(outputParser);
```

.env
```
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=key
LANGSMITH_PROJECT=프로젝트명
OPENAI_API_KEY=key
```

- llama-index-example

라마 인덱스를 사용한 간단한 개발 예제   
문서를 불러옴 -> 색인 생성 -> 질의 엔진 생성 및 질문 생성 -> 색인을 로컬에 저장