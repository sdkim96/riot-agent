from typing import Any
import os

from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from langchain_anthropic.chat_models import ChatAnthropic

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser


from ..utils.knowledge import LLM

class LLMHandler:

    def __init__(self, llm: str) -> None:
        self.llm = llm
        self.api_key = self.get_api_key
        self.llm_model = self.get_llm_model


    async def chat_complete(
        self,
        parser: BaseOutputParser,
        prompt: ChatPromptTemplate,
        input_dict: dict
    ) -> Any:
        chain = prompt | self.llm_model | parser
        return await chain.ainvoke(input_dict)


    @property
    def get_api_key(self) -> str:
        if self.llm == LLM.OPENAI.value:
            return os.getenv("OPENAI_API_KEY")
        elif self.llm == LLM.ANTHROPIC.value:
            return os.getenv("ANTHROPIC_API_KEY")
        else:
            raise ValueError("Invalid LLM! Now only OPENAI and ANTHROPIC are supported.")

    @property
    def get_llm_model(self) -> BaseChatModel:
        if self.llm == LLM.OPENAI.value:
            return ChatOpenAI()
        
        elif self.llm == LLM.ANTHROPIC.value:
            return ChatAnthropic()
    