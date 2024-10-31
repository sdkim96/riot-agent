from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate

class PromptTemplateService:
    
    @staticmethod
    def generate_intent_prompt(
        parser
    ) -> PromptTemplate:
        return PromptTemplate(
            template="""
            Your task is to identify the target intent(s) from the given query.
            Carefully analyze the user's question and provide up to two likely intents (ranked).
            Each intent should include its code and a clear description based on relevance to the query.

            Instructions:
            - Provide the most likely intent as `rank_1_code` and `rank_1_description`.
            - Provide the second most likely intent as `rank_2_code` and `rank_2_description`.
            - Choose the best matches from the list of available intents below.
            - **If only one intent is appropriate, leave rank_2_code and rank_2_description empty.**

            Available Intents (with codes and descriptions):
            {intents}

            Query:
            {query}

            Format Instructions (strict format required):
            {format_instructions}
            """,
            input_variables=['query', 'intents'],
            partial_variables={'format_instructions': parser.get_format_instructions()}
        )