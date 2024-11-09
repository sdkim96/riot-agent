import pytest

from agent.agent import RiotAgent
from agent.skills.task_manager import TaskManager


# @pytest.mark.asyncio
# async def test_get_summoner():
#     agent = RiotAgent(
#         query="페이커가 주로 하는 챔피언이 뭐지?",
#     )
#     tm = TaskManager(agent)
#     await tm._process_summoner()


# @pytest.mark.asyncio
# async def test_get_champion():
#     agent = RiotAgent(
#         query="파이크랑 트리가 어떤 챔프야?",
#     )
#     tm = TaskManager(agent)
#     await tm._get_champion()


@pytest.mark.asyncio
async def test_get_champion():
    agent = RiotAgent(
        query="파이크랑 트리가 어떤 챔프야?",
    )
    tm = TaskManager(agent)
    await tm._get_item()