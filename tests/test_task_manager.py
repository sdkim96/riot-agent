import pytest
from agent.agent import RiotAgent
from agent.skills.task_manager import TaskManager
import cassiopeia as cass

@pytest.mark.asyncio
async def test_get_champion():
    agent = RiotAgent(
        query="파이크랑 트리가 어떤 챔프야?",
    )
    tm = TaskManager(agent)
    await tm._get_champion()