import pytest
from agent.agent import RiotAgent
from agent.externals.riot import RiotHandler


# @pytest.mark.asyncio
# async def test_all_items():
#     riot_handler = RiotHandler(region="KR")
#     items = await riot_handler.get_all_items()
#     assert items

# @pytest.mark.asyncio
# async def test_all_maps():
#     riot_handler = RiotHandler(region="KR")
#     maps = await riot_handler.get_all_maps()
#     assert maps

# @pytest.mark.asyncdio
# async def inititalize_agent():
#     riot_handler = RiotAgent()
#     assert riot_handler

# @pytest.mark.asyncio
# async def test_get_this_patch_version():
#     riot_handler = RiotHandler(region="KR")
#     version = await riot_handler._get_patch_version()
#     assert isinstance(version, str)
#     assert version

# @pytest.mark.asyncio
# async def test_get_champion_by_name():
#     riot_handler = RiotHandler(region="KR")
#     champion = await riot_handler.get_champion_by_name("Jinx")
#     all_lanes = champion.play_rates
    
#     for lane, play_rate in all_lanes.items():
#         play_rate = float(play_rate)
#         print(f"Lane: {lane}, Play Rate: {play_rate}")


# @pytest.mark.asyncio
# async def test_get_op_champions():
#     riot_handler = RiotHandler(region="KR")
#     na_riot_handler = RiotHandler(region="NA")
    
#     kr_champions = await riot_handler.get_all_champions()
#     na_champions = await na_riot_handler.get_all_champions()

#     for nc in na_champions:
#         for kc in kr_champions:
#             if nc.id == kc.id:
#                 print(f"ID: {nc.id}, KR Name: {kc.name}, NA Name: {nc.name}")
#                 break