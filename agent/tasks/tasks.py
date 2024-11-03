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
        pass


    ######################
    # Role-based Analysis #
    ######################

    async def role_based_analysis(agent):
        """
        Recommend champions based on specific team roles like top, jungle, etc.
        """
        pass


    ####################
    # Patch Note Review #
    ####################

    async def patch_note_review(agent):
        """
        Analyze changes in the latest patch and recommend champions based on recent buffs or nerfs.
        """
        pass


    #########################
    # Summoner Growth Tracker #
    #########################

    async def summoner_growth_tracker(agent):
        """
        Track the summoner's progress over seasons for champion mastery and rank.
        """
        pass


    #######################
    # Team Compatibility #
    #######################

    async def team_compatibility(agent):
        """
        Analyze team composition and recommend optimal champions based on compatibility.
        """
        pass


    ######################
    # Match Replay Suggestion #
    ######################

    async def match_replay_suggestion(agent):
        """
        Suggest pro match replays for skill improvement based on user role and champion.
        """
        pass


    ######################
    # Advanced Item Trends #
    ######################

    async def advanced_item_trends(agent):
        """
        Analyze item trends and suggest high-win-rate item builds.
        """
        pass


    #######################
    # Summoner History Analysis #
    #######################

    async def summoner_history_analysis(agent):
        """
        Analyze summoner's past matches to highlight trends and skill progression.
        """
        pass


    ##########################
    # Enemy Matchup Prediction #
    ##########################

    async def enemy_matchup_prediction(agent):
        """
        Predict the rank and likely performance of enemy players in upcoming matches.
        """
        pass


    ######################
    # Champion Mastery Tips #
    ######################

    async def champion_mastery_tips(agent):
        """
        Provide tips on improving champion mastery, focusing on key strengths and weaknesses.
        """
        pass


    ##############################
    # Counter Champions Recommendation #
    ##############################

    async def counter_champions_recommendation(agent):
        """
        Suggest champions that counter the opponent’s team composition.
        """
        pass


    ###########################
    # League of Legends News Feed #
    ###########################

    async def lol_news_feed(agent):
        """
        Provide latest news, updates, and community highlights related to League of Legends.
        """
        pass


    ###############################
    # Ranked Climb Optimization Tips #
    ###############################

    async def ranked_climb_tips(agent):
        """
        Offer tips on optimizing performance in ranked games for consistent progression.
        """
        pass