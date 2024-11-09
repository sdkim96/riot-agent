# import pytest

# from agent.agent import VectorStore, RiotAgent
# from agent.skills.task_manager import TaskManager


# @pytest.mark.asyncio
# async def test_initialize_vectorstore():
#     riot = RiotAgent(
#         query="What is the best champion for mid lane?"
#     )
    
#     test_query = "미드 라인에 가장 좋은 챔피언은 뭐야?"
#     documents = await riot.vectorstore.do_similarity_search(query=test_query, filter={"domain":"intents"})