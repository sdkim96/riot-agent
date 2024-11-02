from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate

from .utils.knowledge import GameModes

class PromptTemplateService:
    
    @staticmethod
    def generate_intent_prompt(parser) -> PromptTemplate:
        return PromptTemplate(
            template="""
                Identify the user's intent from the given query using the provided keywords.
                
                Instructions:
                - Provide up to three intents, ranked by relevance.
                - The primary intent should be filled as `rank_1_code` and `rank_1_description`.
                - If a second intent is relevant, add it as `rank_2_code` and `rank_2_description`.
                - if a third intent is relevant, add it as `rank_3_code` and `rank_3_description`.
                
                - If only one intent is relevant, leave `rank_2_code` and `rank_2_description` and `rank_3_code` and `rank_3_description` None.
                - If two intents are relevant, leave `rank_3_code` and `rank_3_description` None.
                
                Available Intents:
                {intents}

                User Query:
                {query}

                Keywords:
                {keywords}

                Format (strict format required):
                {format_instructions}
            """,
            input_variables=['query', 'intents', 'keywords'],
            partial_variables={'format_instructions': parser.get_format_instructions()}
        )
        
    @staticmethod
    def generate_summoner_prompt(
        parser
    ) -> PromptTemplate:
        return PromptTemplate(
            template="""
            Your task is to extract the summoner name and tag from the user's question. 
            Summoner identifiers are usually in the format `SummonerName#Tag`, where `SummonerName` is the player's name and `Tag` identifies their region or account.

            **Instructions**:
            - Carefully examine the user query for any summoner identifiers in the format `SummonerName#Tag`.
            - If available, also analyze any web search results for additional context.
            - Use the list of known players to confirm or match any extracted identifiers, if relevant.

            **Output Format**:
            - Summoner Name: [Extracted Summoner Name]
            - Tag: [Extracted Tag]

            **Example**:
            - Summoner Name: Hide on Bush
            - Tag: KR1

            **User Query**:
            {query}

            **Web Search Results**:
            {maybe}

            **Known Players**:
            {known_players}

            **Format Instructions** (strict format required):
            {format_instructions}
            """,
            input_variables=['query', 'maybe', 'known_players'],
            partial_variables={'format_instructions': parser.get_format_instructions()}
        )
    
    @staticmethod
    def generate_keywords_prompt(
        parser
    ):
        return PromptTemplate(
            template="""
            Your task is to identify **up to 3 essential keywords** from the user's question. 
            These keywords should help to clearly understand the user's intent and context.

            **Guidelines**:
            1. Only select nouns as keywords.
            2. Limit the keywords to a maximum of 3.
            3. Ensure the keywords capture the main subject and focus of the question.
            
            **User Query**:
            {query}

            **User's Intent**:
            {intents}

            **Format Instructions**:
            {format_instructions}

            For example, if the query is "룰러 선수가 자주 가는 템트리," the keywords should be:
            - 룰러 선수
            - 템트리
            """,
            input_variables=['query', 'intents'],
            partial_variables={'format_instructions': parser.get_format_instructions()}
        )
    
    @staticmethod
    def generate_domain_knowlege_from_keyword():
        return PromptTemplate(
            template="""
            Your task is to provide information based on the extracted keywords from the user's question in main domain.
            The main domain is famous game, 'League of Legends'
            The information should be relevant to the keywords.

            **Guidelines**:
            1. Provide detailed information about the keywords.
            2. Include any relevant statistics, facts, or explanations.
            3. Ensure the information is accurate and up-to-date.
            4. If you are unsure about the information, Return 'No information found.'

            **Keywords**:
            {keywords}

            """,
            input_variables=['keywords'],
        )
    