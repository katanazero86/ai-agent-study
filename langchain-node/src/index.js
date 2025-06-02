import {ChatOpenAI} from "@langchain/openai";
import {PromptTemplate} from "@langchain/core/prompts";
import {StringOutputParser} from "@langchain/core/output_parsers";
import { LangChainTracer } from "langchain/callbacks";
import * as dotenv from "dotenv";

dotenv.config();

// LangChain 트레이서 초기화
const tracer = new LangChainTracer({
    projectName: process.env.LANGSMITH_PROJECT
});

const llm = new ChatOpenAI();
const result = await llm.invoke("Hello, world!", {
    callbacks: [tracer]
});

console.log('hello world!');
console.log(result.content);

const prompt = new PromptTemplate({
    inputVariables: ['flower'],
    template: "{flower}의 꽃말은?"
});

const outputParser = new StringOutputParser();

const chain = prompt.pipe(llm).pipe(outputParser);

// 실행 (트레이싱 포함)
const chainResult = await chain.invoke(
    {
        flower: '장미'
    },
    {
        callbacks: [tracer],
        tags: ["flower-meaning"]
    }
);

console.log(chainResult);