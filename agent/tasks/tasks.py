import asyncio
import random

from ..dto.exceptions import TaskCantBeAdded

############
# Summoner #
############

class TaskPool:


    async def compare_summoners(agent):
        """
        Find the summoner that the user wants to compare.
        """
        print(f"🔍 Finding the summoner that the user wants to compare.")
        try:
            summoners = agent.query.target_summoners
            print(f"🎉 Found the summoners: {summoners}")

            if len(summoners) < 2:
                raise TaskCantBeAdded("Need at least two summoners to compare.")

            summoners_details = []
            for summoner in summoners:
                if summoner is None:
                    raise TaskCantBeAdded("Summoner not found.")
                
                summoners_detail = await agent.riot_handler.get_summoner(summoner)
                summoners_details.append(summoners_detail)

            agent.query.searched_knowledges["summoners"] = summoners_details
        except:
            raise TaskCantBeAdded("Summoners not found.")

        

    ############
    # Champion #
    ############


    async def find_this_patch_op_champions(agent):
        """
        Find the OP champions in this patch.
        """
        print(f"🔍 Finding the OP champions in this patch.")
        try:
            champions = await agent.riot_handler.get_op_champions()
            print(f"🎉 Found the OP champions: {champions}")

            agent.query.searched_knowledges["op_champions"] = champions
        except:
            raise TaskCantBeAdded("OP Champions not found in this patch.")
        


    ##############
    # Item build #
    ##############


    async def find_item_build(agent):
        """
        Find the item build for the given champion.
        """
        print(f"🔍 Finding the item build for the given champion.")
        try:
            item_build = await agent.riot_handler.get_item_build()
            print(f"🎉 Found the item build: {item_build}")
        except:
            raise TaskCantBeAdded("Item build not found.")
        

    ##############
    # Match data #
    ##############


    async def find_match_data(agent):
        """
        Find the match data for the given summoner.
        """
        print(f"🔍 Finding the match data for the given summoner.")
        try:
            match_data = await agent.riot_handler.get_match_data()
            print(f"🎉 Found the match data: {match_data}")
        except:
            raise TaskCantBeAdded("Match data not found.")
    

    ######################
    # Champion Statistics #
    ######################

    async def champion_statistics(agent):
        """
        Retrieve champion statistics such as win rate, pick rate, and ban rate.
        """
        print("📊 Retrieving champion statistics (win rate, pick rate, ban rate)...")
        await asyncio.sleep(random.uniform(1, 3))

    ######################
    # Role-based Analysis #
    ######################

    async def role_based_analysis(agent):
        """
        Recommend champions based on specific team roles like top, jungle, etc.
        """
        print("🔍 Analyzing role-based recommendations (top, jungle, etc.)...")
        await asyncio.sleep(random.uniform(1, 3))

    ####################
    # Patch Note Review #
    ####################

    async def patch_note_review(agent):
        """
        Analyze changes in the latest patch and recommend champions based on recent buffs or nerfs.
        """
        print("📄 Reviewing patch notes and analyzing recent buffs/nerfs...")
        await asyncio.sleep(random.uniform(1, 3))

    #########################
    # Summoner Growth Tracker #
    #########################

    async def summoner_growth_tracker(agent):
        """
        Track the summoner's progress over seasons for champion mastery and rank.
        """
        print("📈 Tracking summoner growth over seasons for mastery and rank...")
        await asyncio.sleep(random.uniform(1, 3))

    #######################
    # Team Compatibility #
    #######################

    async def team_compatibility(agent):
        """
        Analyze team composition and recommend optimal champions based on compatibility.
        """
        print("🤝 Analyzing team composition for optimal compatibility...")
        await asyncio.sleep(random.uniform(1, 3))

    ######################
    # Match Replay Suggestion #
    ######################

    async def match_replay_suggestion(agent):
        """
        Suggest pro match replays for skill improvement based on user role and champion.
        """
        print("🎬 Suggesting pro match replays for skill improvement...")
        await asyncio.sleep(random.uniform(1, 3))

    ######################
    # Advanced Item Trends #
    ######################

    async def advanced_item_trends(agent):
        """
        Analyze item trends and suggest high-win-rate item builds.
        """
        print("📦 Analyzing item trends for high-win-rate builds...")
        await asyncio.sleep(random.uniform(1, 3))

    #######################
    # Summoner History Analysis #
    #######################

    async def summoner_history_analysis(agent):
        """
        Analyze summoner's past matches to highlight trends and skill progression.
        """
        print("📅 Analyzing summoner history to identify trends and progress...")
        await asyncio.sleep(random.uniform(1, 3))

    ##########################
    # Enemy Matchup Prediction #
    ##########################

    async def enemy_matchup_prediction(agent):
        """
        Predict the rank and likely performance of enemy players in upcoming matches.
        """
        print("🎯 Predicting enemy matchups for upcoming matches...")
        await asyncio.sleep(random.uniform(1, 3))

    ######################
    # Champion Mastery Tips #
    ######################

    async def champion_mastery_tips(agent):
        """
        Provide tips on improving champion mastery, focusing on key strengths and weaknesses.
        """
        print("💡 Providing tips to improve champion mastery...")
        await asyncio.sleep(random.uniform(1, 3))

    ##############################
    # Counter Champions Recommendation #
    ##############################

    async def counter_champions_recommendation(agent):
        """
        Suggest champions that counter the opponent’s team composition.
        """
        print("🛡️ Recommending counter champions for opponent's team...")
        await asyncio.sleep(random.uniform(1, 3))

    ###########################
    # League of Legends News Feed #
    ###########################

    async def lol_news_feed(agent):
        """
        Provide latest news, updates, and community highlights related to League of Legends.
        """
        print("📰 Gathering latest League of Legends news and updates...")
        await asyncio.sleep(random.uniform(1, 3))

    ###############################
    # Ranked Climb Optimization Tips #
    ###############################

    async def ranked_climb_tips(agent):
        """
        Offer tips on optimizing performance in ranked games for consistent progression.
        """
        print("📈 Offering ranked climb tips for better progression...")
        await asyncio.sleep(random.uniform(1, 3))