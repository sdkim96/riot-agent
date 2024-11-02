from ...agent import RiotAgent
from ..dto.exceptions import TaskCantBeAdded

############
# Summoner #
############

async def find_this_patch_op_champions(agent: RiotAgent):
    """
    Find the OP champions in this patch.
    """
    print(f"🔍 Finding the OP champions in this patch.")
    try:
        champions = await agent.riot_handler.get_op_champions()
        print(f"🎉 Found the OP champions: {champions}")
    except:
        raise TaskCantBeAdded("OP Champions not found in this patch.")